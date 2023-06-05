#!/usr/bin/env python
# coding: utf-8

import os.path
import warnings
import sys

from setuptools import setup, Command, find_packages

install_requires = [
     "psutil",
     ]

DESCRIPTION = 'Simple monitor'
LONG_DESCRIPTION = 'Simple monitor'

setup(
    name='simple_mon',
    version="0.0.1",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Benoit B',
    author_email='benoit@ðator.lu',
    maintainer='Benoit B.',
    maintainer_email='benoit@ðator.lu',
    license='GPL3',      
    packages=find_packages(),
    install_requires=install_requires,


    classifiers=[
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    script="",
     entry_points={
        'console_scripts': [
            'simple_mon = simple_mon.simple_mon:main',
         ]
    }
)

