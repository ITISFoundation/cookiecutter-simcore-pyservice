""" app's configuration

    This module loads the schema defined by every subsystem and injects it in the
    application's configuration scheams

    It was designed in a similar fashion to the setup protocol of the application
    where every subsystem is imported and queried in a specific order. The application
    depends on the subsystem and not the other way around.

    The app configuration is created before the application instance exists.


TODO: can this be done using declarative programming??
TODO: add more strict checks with re
TODO: add support for versioning.
    - check shema fits version
    - parse/format version in schema
"""
import logging

import trafaret as T
from servicelib import application_keys  # pylint:disable=unused-import
from servicelib.application_keys import APP_CONFIG_KEY

from .resources import resources
from . import rest_config

log = logging.getLogger(__name__)


def create_schema():
    """
        Build schema for the configuration's file
        by aggregating all the subsystem configurations
    """
    schema = T.Dict({
        "version": T.String(),
        "main": T.Dict({
            "host": T.IP,
            "port": T.Int(),
            "log_level": T.Enum(*logging._nameToLevel.keys()), # pylint: disable=protected-access
            "enabled_developmen_mode": T.Bool(),
        }),
        rest_config.CONFIG_SECTION_NAME: rest_config.schema,
        ## Add here more configurations
    })


    section_names = [k.name for k in schema.keys]
    assert len(section_names) == len(set(section_names)), "Found repeated section names in %s" % section_names

    return schema


 # app[APP_CONFIG_KEY] = key for config object
APP_CONFIG_KEY = APP_CONFIG_KEY

# config/${CLI_DEFAULT_CONFIGFILE}
CLI_DEFAULT_CONFIGFILE = 'config-container-prod.yml'

# schema for app config's startup file
app_schema = create_schema()

assert resources.exists( 'config/' + CLI_DEFAULT_CONFIGFILE ), \
        "'config/%s' does not exist" % CLI_DEFAULT_CONFIGFILE
