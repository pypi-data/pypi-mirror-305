# Health Checks for HMLR Flask Applications

## Consistent health endpoints

### Features
* Easy provision of standard /health endpoint
* Nearly easy provision of standard /health/cascade endpoint
* Helpers for web app and PostgreSQL dependencies


This package depends on:
* Flask
* Requests


#### Flask applications
Import `HealthChecks` and initialise it as a Flask extension:


Just enough to get /health working:
```python
from landregistry.healthchecks import HealthChecks
from <somewhere> import app

health = HealthChecks()
health.init_app(app)
```

Adding dependencies for the cascading health check:
```python
DEPENDENCIES = {
    "Postgres": SQLALCHEMY_DATABASE_URI,
    "some-app": 'http://some-app:8080'
}
health.add_dependencies(DEPENDENCIES)
```

#### Caution

This currently doesn't do anything clever with avoiding endpoint collisions. It'll just fail.


#### HealthChecks methods

On initialisation, the extension registers `/health` and `/health/cascade/<x>` endpoints without
futher intervention.

The behaviour of the endpoints is documented in `api/openapi.yml`.

**add_web_dependency(name, uri)**

Add a single web-app dependency. The URI should be the base URI for the service (this extension
will add `/health/cascade/<num>` as required).

**add_dependencies(dict)**

Create a set of standard dependency checks. Supply a dictionary of name/uri pairs. Compatible
with the DEPENDENCIES configuration item from the skeleton application. Will accept a pair with
a name of `postgres` and a value containing a SQLAlchemy connection URI.

**add_dependency(name, callback)**

Create a custom dependency check.

Adds a dependency named `name`. Callback is a function pointer. The supplied function should
return a dictionary (any contents will be added to the healthcheck response body) on success
or raise an exception to indicate failure.

Custom dependency results will appear in the 'db' field of the healthcheck response.

#### Custom dependency example

Somewhere, define your new health check helper method. It must return a dict on success (empty
is OK) and throw an exception on failure.

```python
def one_is_more_than_zero_healthcheck():
    if 1 <= 0:
        raise Exception('The numbers have gone wrong')
    return {}
```

Use this method as a callback in `add_dependency`:
```python
health = HealthChecks(app)

health.add_dependency('one_and_zero', one_is_more_than_zero_healthcheck)
```

Now your application will check that 1 is greater than 0 as part of its cascading healthcheck.


#### Configuration Options

Configure the package behaviour but setting application configuration values (e.g. in `config.py`).

The `/health` and `/health/cacasde/<x>` routes have the following options:

| Option                         | Default | Does what                                                                   |
| ------------------------------ | ------- | --------------------------------------------------------------------------- |
| HEALTH_INCLUDE_REQUEST_HEADERS | False   | If `True`, include request headers in healthcheck response `headers` field. |
