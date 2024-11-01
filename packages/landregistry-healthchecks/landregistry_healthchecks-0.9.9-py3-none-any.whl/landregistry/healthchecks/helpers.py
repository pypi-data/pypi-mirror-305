from datetime import datetime
from typing import cast

from flask import current_app

# Try to import psycopg2 if it's installed. Because we don't want the package to require it,
# fall back to a stub version if it isn't. The stub just raises an exception when called.
try:
    import psycopg2
except ImportError:
    from . import fakepsy as psycopg2  # type: ignore[no-redef]


class HealthcheckError(Exception):
    pass


def postgres_get_timestamp() -> dict[str, str]:
    if "SQLALCHEMY_DATABASE_URI" not in current_app.config:
        raise HealthcheckError("SQLALCHEMY_DATABASE_URI must be set")

    try:
        conn = psycopg2.connect(current_app.config["SQLALCHEMY_DATABASE_URI"])
        cur = conn.cursor()
        cur.execute("SELECT CURRENT_TIMESTAMP;")
        result = cast(list[datetime], cur.fetchone())
        cur.close()
        conn.close()
        return {
            "current_timestamp": result[0].strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        }
    except psycopg2.DataError as e:
        current_app.logger.warning("Input data error: " + str(e))
        raise HealthcheckError("Input data error: " + str(e))
    except (psycopg2.OperationalError, psycopg2.ProgrammingError) as e:
        current_app.logger.warning("Database error: " + str(e))
        raise HealthcheckError("Database error: " + str(e))
