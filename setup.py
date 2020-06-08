#!/usr/bin/env python

# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name='ci_workshop',
    description='A sample application to test GitHub actions',
    author='',
    author_email='',
    url='https://github.com/MaastrichtU-IDS/workshop-ci-template',
    packages=find_packages(include=['ci_workshop']),
    package_dir={'ci_workshop': 'ci_workshop'},
    entry_points={
        'console_scripts': [
            'ci_workshop=ci_workshop.__main__:main',
        ],
    },

    python_requires='>=3.6.0',
    version='0.0.0',
    long_description=readme,
    include_package_data=True,
    install_requires=open("requirements.txt", "r").readlines(),
    license='Mozilla',
)
