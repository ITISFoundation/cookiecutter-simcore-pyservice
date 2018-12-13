""" Configuration of {{ cookiecutter.package_name }}

The application can consume settings revealed at different
stages of the development workflow. This submodule gives access
to all of them.

"""
import logging

from .__version__ import get_version_object

log = logging.getLogger(__name__)

## CONSTANTS--------------------
RESOURCE_KEY_OPENAPI = "oas3/{{ cookiecutter.openapi_specs_version }}"

## BUILD ------------------------
#  - Settings revealed at build/installation time
#  - Only known after some setup or build step is completed
PACKAGE_VERSION = get_version_object()

API_MAJOR_VERSION = PACKAGE_VERSION.major
API_URL_VERSION = "v{:.0f}".format(API_MAJOR_VERSION)


## KEYS -------------------------
# Keys used in different scopes. Common naming format:  
#
#    $(SCOPE)_$(NAME)_KEY
#

# APP=application
APP_CONFIG_KEY="config"

# CFG=configuration

# RSC=resource
RSC_CONFIG_KEY  = "config"
RSC_OPENAPI_KEY = "oas3/{}".format(API_URL_VERSION)


# RQT=request


# RSP=response


## Settings revealed at runtime: only known when the application starts 
#  - via the config file passed to the cli

OAS_ROOT_FILE = "{}/openapi.yaml".format(RSC_OPENAPI_KEY)