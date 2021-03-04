"""``setuptools`` configuration for requirements and packaging."""

import codecs
from pathlib import Path

from setuptools import find_packages, setup

HERE = Path(__file__).parent.absolute()
VERSION = HERE.joinpath('symbio_reference', '__version__.py')
ABOUT = {}

with codecs.open(VERSION, 'r', 'utf-8') as stream:
    exec(stream.read(), ABOUT)

with open(HERE / 'requirements.txt') as f:
    INSTALL_REQS = f.read().splitlines()

setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__description__'],
    url=ABOUT['__url__'],
    author=ABOUT['__author__'],
    author_email=ABOUT['__author_email__'],
    license=ABOUT['__license__'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQS,
    entry_points={
        'console_scripts': [
            'ref = symbio_reference:APP.main',
            'ref-func = symbio_reference.testing.cli:main'
        ]
    }
)
