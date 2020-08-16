#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages

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
    name='design-pytterns',
    version='0.1.0',
    url='https://github.com/Alchemy-Meister/python-design-patterns',
    author='Alchemy-Meister',
    author_email='meister.alchemy@gmail.com',
    license='GPLv3+',
    description="Implementation of Basic Python Design Patters",
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
