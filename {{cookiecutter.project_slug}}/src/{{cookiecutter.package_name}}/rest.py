""" RESTful API for {{ cookiecutter.package_name }} """
import logging

from aiohhtp import web

from rest_handles import check_action, check_health
from servicelib import rest_routes
from servicelib.application_keys import APP_OPENAPI_SPECS_KEY

log = logging.getLogger(__name__)


def setup(app: web.Application):
    """Setup the rest API module in the application in aiohttp fashion. 
    
    """
    log.debug("Setting up %s ...", __name__)

    valid_specs = app[APP_OPENAPI_SPECS_KEY]

    assert valid_specs, "No API specs in app[%s]. Skipping setup %s "% (APP_OPENAPI_SPECS_KEY, __name__)

    routes = rest_routes.create(valid_specs, [check_action, check_health])
    app.router.add_routes(routes)



# alias
setup_rest = setup

__all__ = (
    'setup_rest'
)
