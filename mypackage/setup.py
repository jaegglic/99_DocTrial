#!/usr/bin/env python

import setuptools

with open("..\\README.md", "r") as file_handle:
    long_description = file_handle.read()

setuptools.setup(
    name='doc_trial',
    version='0.0.1',
    description='Automatic documentation test',
    long_description=long_description,
    author='Yes Me',
    author_email='yes.me@mydomain.loc',
    url='https://doc-trial.readthedocs.io/en/latest/',
    packages=setuptools.find_packages(),
)
