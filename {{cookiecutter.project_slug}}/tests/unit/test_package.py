# pylint:disable=wildcard-import
# pylint:disable=unused-import
# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import os
import re
import subprocess
from pathlib import Path

import pytest

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

def test_no_pdbs_in_place(package_dir):
    # TODO: add also test_dir excluding this function!?
    # TODO: it can be commented!
    MATCH = re.compile(r'pdb.set_trace()')
    EXCLUDE = ["__pycache__", ".git"]
    for root, dirs, files in os.walk(package_dir):
        for name in files:
            if name.endswith(".py"):
                pypth = (Path(root) / name)
                code = pypth.read_text()
                found = MATCH.findall(code)
                assert not found, "pbd.set_trace found in %s" % pypth
        dirs[:] = [d for d in dirs if d not in EXCLUDE]

# TODO run entrypoint with subprocess since it check dependency conflicts upon load_entrypoint!
