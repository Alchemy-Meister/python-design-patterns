#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Package distribution based on setuptools."""

from os.path import abspath, dirname, join
from setuptools import setup, find_packages

about = {}

with open(
        join(dirname(abspath(__file__)), 'src/design_pytterns/_about.py'), 'r'
) as about_file:
    exec(about_file.read(), about)  # nosec

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

install_requires = []

tests_require = [
    'coverage',
    'pytest',
    'pytest-cov'
]

extras_require = {'tests': tests_require}

setup(
    name=about['__title__'],
    version=about['__version__'],
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    license=about['__license__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords="Design Patterns, Singleton, Factory, Observer",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        "Operating System :: OS Independent"
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require
)
