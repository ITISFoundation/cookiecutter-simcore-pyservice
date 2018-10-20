# pylint:disable=wildcard-import
# pylint:disable=unused-import
# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

from pathlib import Path

import pkg_resources
import pytest
import yaml

from openapi_spec_validator import validate_spec
from openapi_spec_validator.exceptions import OpenAPIValidationError

import {{ cookiecutter.package_name }}


API_VERSIONS = ('{{ cookiecutter.openapi_specs_version }}', )

@pytest.fixture
def spec_basepath():
    basepath = Path(pkg_resources.resource_filename({{ cookiecutter.package_name }}.__name__, 'oas3'))
    assert basepath.exists()
    return basepath


@pytest.mark.parametrize('version', API_VERSIONS)
def test_specifications(spec_basepath, version):

    spec_path = spec_basepath / "{}/openapi.yaml".format(version)

    with spec_path.open() as fh:
        specs = yaml.load(fh)
        try:
            validate_spec(specs, spec_url=spec_path.as_uri())
        except OpenAPIValidationError as err:
            pytest.fail(err.message)
