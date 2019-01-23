""" Access to data resources installed within this package

"""
from typing import Dict

import pkg_resources

from servicelib.resources import ResourcesFacade

_META_PKG_INFO = 'PKG-INFO'

resources = ResourcesFacade(
    package_name=__name__,
    distribution_name="{{ cookiecutter.distribution_name }}",
    config_folder='config',
)

def get_distribution_info() -> Dict:
    """ Returns distributon information, as  provided in setup """
    dist = pkg_resources.get_distribution('{{ cookiecutter.distribution_name }}')
    info = dist.get_metadata(_META_PKG_INFO) if dist.has_metadata(_META_PKG_INFO) else {}
    return info


__all__ = (
    'resources',
    'get_distribution_info'
)
