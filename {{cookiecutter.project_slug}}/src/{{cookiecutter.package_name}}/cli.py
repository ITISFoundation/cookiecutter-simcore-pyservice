"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m{{cookiecutter.package_name}}` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.

"""
import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Dict

import trafaret_config.commandline as trafaret_config_cmd
from servicelib.utils import search_osparc_repo_dir

from .__version__ import __version__
from .application import run_service
from .application_config import CLI_DEFAULT_CONFIGFILE, app_schema
from .resources import get_distribution_info, resources

here = Path(sys.argv[0] if __name__ =="__main__" else __file__).resolve().parent
log = logging.getLogger(__name__)


def create_default_parser():
    pkg_name = "{} {}".format(__package__.split(".")[0], __version__)
    desc = get_distribution_info().get('description', '')
    return argparse.ArgumentParser(description="%s %s" % (pkg_name, desc))


def setup_parser(args_parser):
    """
        Adds settings group to cli with options:

        -c CONFIG, --config CONFIG
                                Configuration file (default: 'config.yaml')
        --print-config        Print config as it is read after parsing and exit
        --print-config-vars   Print variables used in configuration file
        -C, --check-config    Check configuration and exit
    """
    trafaret_config_cmd.standard_argparse_options(
        args_parser.add_argument_group('settings'),
        default_config=CLI_DEFAULT_CONFIGFILE)

    # Add here more options ....

    return args_parser


def create_environ(*, skip_host_environ: bool = False) -> Dict[str, str]:
    """ Build environment with substitutable variables


    :param skip_host_environ: excludes os.environ , defaults to False
    :param skip_host_environ: bool, optional
    :return: a dictionary of variables to replace in config file
    :rtype: Dict[str, str]
    """

    # system's environment variables
    environ = dict() if skip_host_environ else dict(os.environ)

    # project-related environment variables
    rootdir = search_osparc_repo_dir(here)
    if rootdir is not None:
        environ.update({
            'OSPARC_SIMCORE_REPO_ROOTDIR': str(rootdir),
        })

    return environ


def config_from_options(options, vars=None):  # pylint: disable=W0622
    if vars is None:
        vars = os.environ

    if not os.path.exists(options.config):
        resource_name = options.config
        if resources.exists(resource_name):
            options.config = resources.get_path(resource_name)
        else:
            resource_name = resources.config_folder + '/' + resource_name
            if resources.exists(resource_name):
                options.config = resources.get_path(resource_name)

    log.debug("Loading '%s'", options.config)

    return trafaret_config_cmd.config_from_options(options, trafaret=app_schema, vars=vars)


def run_parser(args_parser, args) -> Dict:
    """ Parse options and returns a configuration object """
    if args is None:
        args = sys.argv[1:]

    # ignore unknown options
    options, _ = args_parser.parse_known_args(args)

    config = config_from_options(options, vars=create_environ())
    return config


def main(args=None):
    args_parser = create_default_parser()

    setup_parser(args_parser)
    config = run_parser(args_parser, args)

    # TODO: improve keys!
    log_level = config["main"]["log_level"]
    logging.basicConfig(level=getattr(logging, log_level))

    run_service(config)

    logging.debug(
        "{{ cookiecutter.command_line_interface_bin_name }} %s", args)
