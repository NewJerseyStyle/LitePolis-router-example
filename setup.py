# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='litepolis-router-example',
    version="0.0.1",
    description='Example router module for LitePolis with database integration',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='NewJerseyStyle',
    # author_email='your@email.com',
    url='https://github.com/NewJerseyStyle/LitePolis-router-example',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'fastapi',
        'litepolis',
        'litepolis-database-example',
    ],
)
