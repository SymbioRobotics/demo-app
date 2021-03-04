"""Entry point for running functional tests."""

from symbio.testing.functional import FunctionalTestRunner

from symbio_reference import APP


main = FunctionalTestRunner(test_modules=APP.conf.FUNCTIONAL_TEST_MODULES).main
