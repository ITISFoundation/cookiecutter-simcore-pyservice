# pylint:disable=wildcard-import
# pylint:disable=unused-import
# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import pytest
import subprocess

from {{ cookiecutter.package_name }}.cli import main


@pytest.fixture
def pylintrc(osparc_simcore_root_dir):
    pylintrc = osparc_simcore_root_dir / ".pylintrc"
    assert pylintrc.exists()
    return pylintrc


# TODO: check pytst-pylint and replace this test
def test_run_pylint(pylintrc, package_dir):
    cmd = 'pylint -j 2 --rcfile {} -v {}'.format(pylintrc, package_dir)
    assert subprocess.check_call(cmd.split()) == 0


def test_main(here): # pylint: disable=unused-variable
    """
        Checks cli in place
    """
    with pytest.raises(SystemExit) as excinfo:
        main("--help".split())
    
    # TODO: check at least config file 
    assert excinfo.value.code == 0


# TODO run entrypoint with subprocess since it check dependency conflicts upon load_entrypoint!