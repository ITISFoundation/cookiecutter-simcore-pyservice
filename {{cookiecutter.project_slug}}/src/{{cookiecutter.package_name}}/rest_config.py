""" rest subsystem's configuration

    - constants
    - config-file schema
"""
import trafaret as T

from servicelib.application_keys import APP_OPENAPI_SPECS_KEY

APP_OPENAPI_SPECS_KEY = APP_OPENAPI_SPECS_KEY    # pylint: disable=self-assigning-variable, bad-option-value

CONFIG_SECTION_NAME = 'rest'

schema = T.Dict({
    "version": T.Enum("{{cookiecutter.openapi_specs_version}}"),
    "location": T.Or(T.String, T.URL),   # either path or url should contain version in it
})
