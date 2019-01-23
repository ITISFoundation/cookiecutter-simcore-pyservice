# pylint:disable=wildcard-import
# pylint:disable=unused-import
# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import sys
from pathlib import Path

import pytest

from servicelib.utils import search_osparc_repo_dir


@pytest.fixture
def here():
    return Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent

@pytest.fixture(scope='session')
def osparc_simcore_root_dir():
    root_dir = search_osparc_repo_dir()
    assert root_dir and root_dir.exists(), "Is this service within osparc-simcore repo?"
    assert any(root_dir.glob("services/{{ cookiecutter.project_slug }}")), "%s not look like rootdir" % root_dir
    return root_dir
