from setuptools import setup, find_packages
from typing import Final

NAME = 'my_package_jenson_2'
VERSION = '0.0.1'
DESCRIPTION = 'My First Python Package'

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    description=DESCRIPTION,
    author='JENSON',
    install_requires=[], 
)
