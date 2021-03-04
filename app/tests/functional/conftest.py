"""
Load the plugin that makes functional tests run within ``pytest``.

This was originally done with setuptools, however the plugin's presence
breaks coverage reports.
https://github.com/pytest-dev/pytest/issues/935
"""

pytest_plugins = 'symbio.testing.functional.pytest_plugin'
