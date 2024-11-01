from typing import Any

import requests
from flask import Request, current_app

from .dependency import Dependency
from .helpers import postgres_get_timestamp


def basic_healthcheck(request: Request) -> dict[str, Any]:
    health_response = {
        "app": current_app.config["APP_NAME"],
        "status": "OK",
        "commit": current_app.config["COMMIT"],
    }

    if current_app.config.get("HEALTH_INCLUDE_REQUEST_HEADERS", False):
        health_response["headers"] = request.headers.to_wsgi_list()

    return health_response


def web_check(dependency: Dependency) -> dict[str, Any]:
    if dependency.uri is None:
        return no_check(dependency)
    return _web_check(dependency.depth, dependency.uri)


def _web_check(depth: int, uri: str) -> dict[str, Any]:
    if uri[-1] != "/":
        uri += "/"

    endpoint = "{}/health/cascade/{}".format(uri, depth)
    current_app.logger.debug("Checking " + endpoint)
    service: dict[str, Any] = {
        "type": "http",
        "status_code": None,
        "content_type": None,
        "content": None,
    }

    try:
        response = requests.get(endpoint)
    except ConnectionAbortedError as e:
        current_app.logger.error(
            "Connection Aborted during health cascade on attempt to connect to {}; full error: {}".format(
                uri, e
            )
        )
        service["status"] = "UNKNOWN"
    except Exception as e:
        current_app.logger.error(
            "Unknown error occured during health cascade on request to {}; full error: {}".format(
                uri, e
            )
        )
        service["status"] = "UNKNOWN"
    else:
        service["status_code"] = response.status_code
        service["content_type"] = response.headers["content-type"]
        service["content"] = response.json()
        if (
            response.status_code == 200
        ):  # Happy route, happy service, happy status_code.
            service["status"] = "OK"
        elif response.status_code == 500:  # Something went wrong
            service["status"] = "BAD"
        else:  # Who knows what happened.
            service["status"] = "UNKNOWN"

    return service


def postgres_check(dependency: Dependency) -> dict[str, Any]:
    try:
        postgres_check = postgres_get_timestamp()
        postgres_check["status"] = "OK"
        return postgres_check
    except Exception as e:
        return {"status": "BAD", "error": str(e)}


def no_check(dependency: Dependency) -> dict[str, Any]:
    return {}


def custom_check(dependency: Dependency) -> dict[str, Any]:
    if dependency.custom_check is None:
        return no_check(dependency)

    try:
        custom_result = dependency.custom_check()
        custom_result["status"] = "OK"
        return custom_result
    except Exception as e:
        return {"status": "BAD", "error": str(e)}
