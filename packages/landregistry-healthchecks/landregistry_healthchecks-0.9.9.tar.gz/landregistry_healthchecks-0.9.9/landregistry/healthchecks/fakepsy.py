"""Fake Psycopg2

This module stubs just enough of Psycopg2 to be called by the Postgres healthcheck helper. It just raises
an exception if it is used.
"""


class HealthcheckUnavailableError(Exception):  # pragma: no cover
    pass


class DataError(Exception):  # pragma: no cover
    pass


class OperationalError(Exception):  # pragma: no cover
    pass


class ProgrammingError(Exception):  # pragma: no cover
    pass


def connect(_noop: str) -> None:  # pragma: no cover
    raise HealthcheckUnavailableError("Psycopg2 is required for this healthcheck")
