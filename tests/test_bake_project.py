# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from .utils import inside_dir

logger = logging.getLogger(__name__)
current_dir = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent


def test_project_tree(cookies):
    result = cookies.bake(extra_context={'project_slug': 'test_project'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_project'
    assert result.project.isdir()


# TODO: use pylint via package instead of application entrypoint
def test_run_pylint(cookies, pylintrc):
    result = cookies.bake(extra_context={'project_slug': 'pylint_compat', 'package_name': 'package_folder'})
    with inside_dir(str(result.project)):
        cmd = 'pylint --rcfile {} -v src/package_folder/'.format(pylintrc.absolute()).split()
        assert subprocess.check_call(cmd) == 0


def test_no_tags(cookies):
    exclude = ['.pylintrc']
    result = cookies.bake(extra_context={
                          'project_slug': 'myproject', 'package_name': 'package_folder'})
    for root, dirs, files in os.walk(result.project):
        for fname in files:
            if fname not in exclude:
                fpath = os.path.join(root, fname)
                with open(fpath) as fh:
                    for lineno, line in enumerate(fh):
                        assert "TODO" not in line, "{}:{}".format(fpath, lineno)
        # skips
        dirs[:] = [n for n in dirs if not n.startswith('.')]


def test_run_tests(cookies):
    result = cookies.bake(extra_context={'project_slug': 'dummy-project'})
    working_dir = str(result.project)
    commands = (
        "ls -la .",
        "pip install pip-tools",
        "make requirements",
        "make install-ci",
        "make test"
    )
    with inside_dir(working_dir):
        for cmd in commands:
            logger.info("Running '%s' ...", cmd)
            assert subprocess.check_call(cmd.split()) == 0
            logger.info("Done '%s' .", cmd)




@pytest.mark.skip("TODO: Under development")
def test_build_docker(cookies, tmpdir):
    # TODO: check build target base, build, cache, prod and devel

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


@pytest.mark.skip("TODO: Under development")
def test_run_docker(cookies, tmpdir):
    # check state after boot
    # check run permissions `simcore-service-storage --help`
    # check load config `simcore-service-storage -c `
    pass
