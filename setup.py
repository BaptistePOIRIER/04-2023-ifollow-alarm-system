# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='app',
    version='1.0.0',
    description='A simple alarm system made with Python for iFollow techical test interview',
    long_description=long_description,
    author='Baptiste POIRIER',
    author_email='baptiste.poirier@efrei.net',
    url='https://github.com/BaptistePOIRIER/04-2023-ifollow-alarm-system',
    packages=find_packages(include=['src', 'test']),
    install_requires=[
        'keyboard==0.13.5',
        'colorama==0.4.5'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)