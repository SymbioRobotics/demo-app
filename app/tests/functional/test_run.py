"""Glue to dynamically generate tests from the ``FunctionalTestRunner``."""

from symbio_reference import APP  # noqa: F401


def test_generator(test_shim, variant):
    """Execute discovered variants."""

    assert test_shim([variant]) == 0
