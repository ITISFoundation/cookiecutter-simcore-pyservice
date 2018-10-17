""" RESTful API for {{ cookiecutter.package_name }} """
import logging

from aiohhtp import web


log = logging.getLogger(__name__)


def setup(app: web.Application):
    """Setup the rest API module in the application in aiohttp fashion. 
    
    """
    log.debug("Setting up %s ...", __name__)





# alias
setup_rest = setup

__all__ = (
    'setup_rest'
)