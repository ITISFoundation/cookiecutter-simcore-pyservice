# TODO: W0611:Unused import ...
# pylint: disable=W0611
# TODO: W0613:Unused argument ...
# pylint: disable=W0613
from pathlib import Path

from {{ cookiecutter.package_name }}.cli import main


@pytest.fixture
def here():
    return Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent


def test_main():
    main([])
