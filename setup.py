#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020-2022 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Package distribution based on setuptools."""

from __future__ import annotations

from os.path import abspath, dirname, join
from typing import Any, Dict

from setuptools import setup, find_packages

about: Dict[str, Any] = {}

with open(
        join(dirname(abspath(__file__)), 'src/design_pytterns/_about.py'),
        'r',
        encoding='utf-8'
) as about_file:
    exec(about_file.read(), about)  # nosec

with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

install_requires = []

extras_require = {
    'docs': [
        'sphinx >= 4.4.0, <5',
        'sphinx_theme >= 1.0, <2'
    ],
    'tests': [
        'coverage >= 6.3.1, <7',
        'pytest >= 7.0.1, <8',
        'pytest-cov >= 3.0.0, <4'
    ]
}

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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
        "Operating System :: OS Independent"
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=install_requires,
    extras_require=extras_require
)
