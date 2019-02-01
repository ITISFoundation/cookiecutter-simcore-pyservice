""" All exceptions used in the {{ cookiecutter.package_name }} code base are defined here.

"""

class ServiceException(Exception):
    """
    Base exception class. All service-specific exceptions should subclass
    this class.
    """
