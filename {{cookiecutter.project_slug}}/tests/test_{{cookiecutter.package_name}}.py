# TODO: W0611:Unused import ...
# pylint: disable=W0611
# TODO: W0613:Unused argument ...
# pylint: disable=W0613

import pytest

from {{ cookiecutter.package_name }}.cli import main

def test_main(here): # pylint: disable=unused-variable    
    main("--help".split())
