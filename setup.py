#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pathlib import Path


setup(
    name="testpackagepypi",
    version="0.1.0",
    url=" ",
    license='MIT',

    author="Dominik Haitz",
    author_email="dominik.haitz at ...",

    description="test",
    long_description=Path('README.md').open().read(),
    long_description_content_type="text/markdown",

    packages=["testpackagepypi"],

    # Derive version from git. If HEAD is at the tag, the version will be the tag itself.
    version_config={
        "version_format": "{tag}.dev{sha}",
        "starting_version": "0.0.1"
    },
    setup_requires=Path('requirements.txt').open().read(),

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
)
