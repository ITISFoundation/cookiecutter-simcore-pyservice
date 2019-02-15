#pylint: disable=W0621
# W0621:Redefining name 'here' from outer scope (line 12)
import logging
import os
import shutil
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import pytest

logger = logging.getLogger(__name__)

@pytest.fixture
def here():
    return Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent

@pytest.fixture
def pylintrc(here):
    path = here.parent / ".pylintrc"
    assert path.exists()
    return path


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        logger.info("CWD now '%s'", dirpath)
        os.chdir(dirpath)
        yield
    finally:
        logger.info("CWD now '%s'", old_path)
        os.chdir(old_path)




def test_project_tree(cookies):
    result = cookies.bake(extra_context={'project_slug': 'test_project'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_project'
    assert result.project.isdir()

# TODO: activate flake8 together with pylint. Need a config file first...
#def test_run_flake8(cookies):
#    result = cookies.bake(extra_context={'project_slug': 'flake8_compat'})
#    with inside_dir(str(result.project)):
#        assert subprocess.check_call(['flake8']) == 0

def test_run_pylint(cookies, pylintrc):
    result = cookies.bake(extra_context={'project_slug': 'pylint_compat', 'package_name': 'package_folder'})
    with inside_dir(str(result.project)):
        cmd = 'pylint --rcfile {} -v src/package_folder/'.format(pylintrc.absolute()).split()
        assert subprocess.check_call(cmd) == 0


def test_run_tests(cookies):
    result = cookies.bake(extra_context={'project_slug': 'dummy-project'})
    working_dir = str(result.project)
    commands = (
        "ls -la .",
        "pip install pip-tools",
        "make requirements",
        "make install",
        "make test"
    )
    with inside_dir(working_dir):
        for cmd in commands:
            logger.info("Running '%s' ...", cmd)
            assert subprocess.check_call(cmd.split()) == 0
            logger.info("Done '%s' .", cmd)



def test_docker_builds(cookies, tmpdir):
    # bakes cookie within osparc-simcore tree structure
    result = cookies.bake(extra_context={'project_slug': 'dummy-project'})
    working_dir = str(result.project)

    tmpdir.mkdir("packages").join("dummy.py").write("import os")
    new_working_dir = tmpdir.mkdir("services") / os.path.basename(working_dir)
    shutil.move(working_dir, new_working_dir)

    # ----
    commands = (
        "ls -la .",
        "pip install pip-tools",
        "make requirements",
        "docker build -f Dockerfile -t dummy-project:prod --target production ../../"
    )
    with inside_dir(new_working_dir):
        for cmd in commands:
            logger.info("Running '%s' ...", cmd)
            assert subprocess.check_call(cmd.split()) == 0
            logger.info("Done '%s' .", cmd)
