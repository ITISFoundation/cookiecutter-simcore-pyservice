# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import sys
from pathlib import Path

import pytest

current_dir = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent

@pytest.fixture
def pylintrc():
    path = current_dir.parent / ".pylintrc"
    assert path.exists()
    return path