""" Main's application module for {{ cookiecutter.package_name }}

"""
from aiohttp import web

def create(config):
    app = web.Application()

    return app

def run(config, app=None):
    if not app:
        app = create(config)

    web.run_app(app,
                host=config["app"]["host"],
                port=config["app"]["port"])
