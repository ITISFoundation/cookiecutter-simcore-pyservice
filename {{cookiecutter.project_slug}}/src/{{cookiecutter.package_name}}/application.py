""" Main's application module for {{ cookiecutter.package_name }} service

    Functions to create, setup and run an aiohttp application provided a configuration object
"""
import json
import logging
from typing import Dict
from aiohttp import web
{%- if cookiecutter.enable_aiohttp_swagger == 'true' %}
from aiohttp_swagger import setup_swagger
{%- endif %}

from .rest import setup_rest
from .application_config import APP_CONFIG_KEY

logger = logging.getLogger(__name__)


def create_application(config: Dict) -> web.Application:
    """
        Initializes service
    """
    logger.debug("Initializing app ... ")

    app = web.Application()
    app[APP_CONFIG_KEY] = config

    is_devmode = config["main"]["enabled_development_mode"]
    if is_devmode:
        logger.debug("Config:\n%s",
            json.dumps(config, indent=2, sort_keys=True))


    {# TODO: here goes every package/plugin setups #}
    setup_rest(app, devel=is_devmode)

    {%- if cookiecutter.enable_aiohttp_swagger == 'true' %}
    setup_swagger(app,
                  title="{{ cookiecutter.distribution_name }}",
                  description="{{ cookiecutter.project_short_description }}",
                  api_version="{{ cookiecutter.version }}",
                  contact="{{ '{full_name} ({github_username})'.format(**cookiecutter) }}",
                  swagger_url="/api/{{ cookiecutter.openapi_specs_version }}/doc")
    {%- endif %}
    return app


def run_service(config: Dict) -> web.Application:
    """ Runs service = creates and runs application

    """
    logger.debug("Serving app ... ")

    app = create_application(config)
    web.run_app(app,
                host=config["main"]["host"],
                port=config["main"]["port"])
    return app

__all__ = (
    'create_application',
    'run_service'
)
