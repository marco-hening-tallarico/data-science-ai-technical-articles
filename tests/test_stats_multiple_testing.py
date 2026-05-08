"""Basic tests for multiple-testing correction helpers."""

from shared.stats.multiple_testing import bonferroni_adjust


def test_bonferroni_adjustment_monotonic_clip() -> None:
    adjusted = bonferroni_adjust([0.001, 0.02, 0.5])
    assert adjusted[0] == 0.003
    assert adjusted[-1] == 1.0
