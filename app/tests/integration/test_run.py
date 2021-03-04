import pytest

from symbio_reference import APP


def test_run():

    # Verify that CLI runs cleanly.

    with pytest.raises(SystemExit):
        APP.main(['info'])
