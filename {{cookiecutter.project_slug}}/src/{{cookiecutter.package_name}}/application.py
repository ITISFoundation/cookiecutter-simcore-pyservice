""" Main's application module for {{ cookiecutter.package_name }} service

    Functions to create, setup and run an aiohttp application provided a configuration object
"""
import logging

from aiohttp import web

from .settings import APP_CONFIG_KEY

log = logging.getLogger(__name__)

def create(config):
    log.debug("Initializing ... ")

    app = web.Application()
    app[APP_CONFIG_KEY] = config


    # TODO: here goes every package/plugin setups

    return app

def run(config, app=None):
    log.debug("Serving app ... ")
    if not app:
        app = create(config)

    web.run_app(app, 
        host=config["main"]["host"], 
        port=config["main"]["port"])
