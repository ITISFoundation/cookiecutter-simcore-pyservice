import logging
import os
from contextlib import contextmanager
from pathlib import Path

logger = logging.getLogger(__name__)


@contextmanager
def inside_dir(dirpath: Path):
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
