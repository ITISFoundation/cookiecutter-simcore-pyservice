#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
from pathlib import Path
from setuptools import setup, find_packages

if sys.version_info.major != 3 and sys.version_info.minor != 6:
    raise RuntimeError("Expected ~=3.6, got %s. Did you forget to activate virtualenv?" % str(sys.version_info))


current_dir = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent
comment_pattern = re.compile(r'^\s*#')

readme = (current_dir/'README.md').read_text()

install_requirements = [
    'aiohttp',
    'trafaret',
    'tenacity',
    'simcore-service-library', # pip install -e git+https://github.com/ITISFoundation/osparc-simcore.git@master#egg=servicelib\&subdirectory=packages/service-library
]

test_requirements = [
    'pytest',
    'pytest-aiohttp', 'pytest-cov',
    'openapi_spec_validator', 
    'pyyaml>=4.2b1', # https://nvd.nist.gov/vuln/detail/CVE-2017-18342
]

kwargs = dict(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
    # FIXME: 'Real Name' (github_name) !!
    author={{ '{0!r}'.format(cookiecutter.full_name).lstrip('ub')}},
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    long_description=readme,
    license="MIT license",
    python_requires='~=3.6',
    packages=find_packages(where='src'),
    package_dir={
        '': 'src',
    },
    package_data={
        '': [
            'config/*.yaml',
            ],
    },
    include_package_data=True,
    install_requires= install_requirements,    
    test_suite='tests',
    tests_require=test_requirements,
    extras_require= {
        'test': test_requirements
    },
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.command_line_interface_bin_name }} = {{ cookiecutter.package_name }}.cli:main',
        ],
    },
)


def main():
    """ Execute the setup commands.

    """
    setup(**kwargs)
    return 0 # syccessful termination

if __name__ == "__main__":
    raise SystemExit(main())
