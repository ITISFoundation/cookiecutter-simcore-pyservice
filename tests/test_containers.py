# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import logging
import shutil
import subprocess
from pathlib import Path
from typing import Tuple

import pytest

from .utils import inside_dir

PROJECT_SLUG = "myservice"

logger = logging.getLogger(__name__)


@pytest.fixture
def simcore_tree(cookies, tmpdir):
    """
        bakes cookie, moves it into a osparc-simcore tree structure with
        all the stub in place
    """
    result = cookies.bake(extra_context={
        'project_slug': PROJECT_SLUG,
        'github_username': 'pcrespov'
    })
    workdir = Path(result.project).resolve()

    template_dir = workdir / "_osparc-simcore-stub"
    simcore_dir = tmpdir / "osparc-simcore"
    template_dir.rename(simcore_dir)

    service_dir = simcore_dir / "services/{}".format(PROJECT_SLUG)
    shutil.rmtree(service_dir)
    workdir.rename(service_dir)

    return (simcore_dir, service_dir)



@pytest.mark.skip("TODO: Under development")
def test_docker_builds(simcore_tree: Tuple[Path]):
    simcore_dir, service_dir = simcore_tree

    with inside_dir(service_dir):
        commands = (
            "ls -la .",
            "pip install pip-tools",
            "make requirements"
        )
        for cmd in commands:
            logger.info("Running '%s' ...", cmd)
            assert subprocess.check_call(cmd.split()) == 0
            logger.info("Done '%s' .", cmd)


    # TODO: check build target base, build, cache, prod and devel
    with inside_dir(simcore_dir / "services"):
        commands = (
            "ls -la .",
            "docker-compose build %s" % PROJECT_SLUG,
            "docker-compose -f docker-compose.yml -f docker-compose.devel.yml build %s" % PROJECT_SLUG
        )
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
