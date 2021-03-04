"""Public interface definition for this package."""
from symbio.dcs.app import Application
from symbio.testing import interactive_logging

from symbio_reference import testing
from symbio_reference.__version__ import (
    __author__,
    __author_email__,
    __copyright__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__
)

APP = Application(name=__title__, functional_test_modules=[testing],
                  logging_conf=interactive_logging())

__all__ = (
    'APP',
)
