import datetime
import json
from typing import Any, Callable, Literal, Optional

from flask import Flask, Response, current_app, request

from .checks import basic_healthcheck, custom_check, no_check, postgres_check, web_check
from .dependency import Dependency, DependencyType


class HealthChecks(object):
    def __init__(self: "HealthChecks", app: Optional[Flask] = None) -> None:
        self.app = app
        self.dependencies: list[Dependency] = []
        if app is not None:
            self.init_app(app)

    def init_app(self: "HealthChecks", app: Flask) -> None:
        @app.route("/health", methods=["GET"])
        def get_health() -> Response:
            result = basic_healthcheck(request)
            return Response(
                response=json.dumps(result), mimetype="application/json", status=200
            )

        @app.route("/health/cascade/<str_depth>")
        def get_health_cascade(str_depth: str) -> Response:
            depth = int(str_depth)
            services: list[dict[str, Any]] = []
            dbs: list[dict[str, Any]] = []

            overall_status: Literal[200, 500] = 200
            if depth > 0:
                for dependency in self.dependencies:
                    if dependency.type == DependencyType.WEB:
                        dependency.depth = depth - 1

                    result = dependency.check(dependency)
                    if (
                        not result
                    ):  # Gloss over any empty dictionaries e.g. from no_check
                        continue

                    if result["status"] != "OK":
                        overall_status = 500

                    if "name" not in result:
                        result["name"] = dependency.name

                    if dependency.type == DependencyType.WEB:
                        services.append(result)
                    else:
                        dbs.append(result)

            response_json = {
                "cascade_depth": depth,
                "server_timestamp": str(datetime.datetime.now()),
                "app": current_app.config.get("APP_NAME"),
                "status": "BAD" if overall_status == 500 else "OK",
                "commit": current_app.config.get("COMMIT"),
                "db": dbs,
                "services": services,
            }

            if current_app.config.get("HEALTH_INCLUDE_REQUEST_HEADERS", False):
                response_json["headers"] = request.headers.to_wsgi_list()

            return Response(
                response=json.dumps(response_json),
                mimetype="application/json",
                status=overall_status,
            )

    def add_web_dependency(self: "HealthChecks", name: str, uri: str) -> None:
        dependency = Dependency(name, DependencyType.WEB, web_check)
        dependency.uri = uri

        self.dependencies.append(dependency)

    def add_dependencies(self: "HealthChecks", dictionary: dict[str, Any]) -> None:
        for key, value in dictionary.items():
            if key.upper() == "POSTGRES":
                self._add_dependency("postgres", postgres_check)
            else:
                self.add_web_dependency(key, value)

    def add_dependency(self, name: str, callback: Callable[[], dict[str, Any]]) -> None:
        dependency = Dependency(name, DependencyType.DB, custom_check)
        dependency.custom_check = callback
        self.dependencies.append(dependency)

    def _add_dependency(
        self: "HealthChecks",
        name: str,
        callback: Optional[Callable[[Dependency], dict[str, Any]]],
    ) -> None:
        actual_callback = callback
        if actual_callback is None:
            actual_callback = no_check

        self.dependencies.append(Dependency(name, DependencyType.DB, actual_callback))
