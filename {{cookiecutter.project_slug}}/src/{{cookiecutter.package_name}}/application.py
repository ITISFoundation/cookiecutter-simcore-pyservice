""" Main's application module for {{ cookiecutter.package_name }} service

    Functions to create, setup and run an aiohttp application provided a configuration object
"""
import json
import logging
from typing import Dict
from aiohttp import web

from .rest import setup_rest
from .application_config import APP_CONFIG_KEY

log = logging.getLogger(__name__)


def create_application(config: Dict) -> web.Application:
    """
        Initializes service
    """
    log.debug("Initializing app ... ")

    app = web.Application()
    app[APP_CONFIG_KEY] = config

    is_devmode = config["main"]["enabled_developmen_mode"]
    if is_devmode:
        log.debug("Config:\n%s",
            json.dumps(config, indent=2, sort_keys=True))


    # TODO: here goes every package/plugin setups
    setup_rest(app, devel=is_devmode)

    return app


def run_service(config: Dict) -> web.Application:
    """ Runs service = creates and runs application

    """
    log.debug("Serving app ... ")

    app = create_application(config)
    web.run_app(app,
                host=config["main"]["host"],
                port=config["main"]["port"])
    return app

__all__ = (
    'create_application',
    'run_service'
)
