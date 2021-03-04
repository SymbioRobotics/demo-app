"""Minimal functional test to demonstrate usage."""

from typing import Any, List

from symbio.testing.functional import FunctionalTest


class MyTest(FunctionalTest):

    """Dummy test."""

    def run_variant(self, *args: Any, **kwargs: Any) \
            -> FunctionalTest.VariantResult:
        """Do nothing."""

        return FunctionalTest.VariantResult(
            success=True, metrics={}, time_series={})

    def _list_variants(self, *args: Any) -> List[str]:
        return ['1']
