"""Article-specific helpers for multiple-testing corrections."""

from __future__ import annotations

import numpy as np


def bonferroni_adjust(p_values: list[float] | np.ndarray) -> np.ndarray:
    """Return Bonferroni-adjusted p-values clipped to [0, 1]."""
    p_array = np.array(p_values, dtype=float)
    return np.minimum(1.0, p_array * len(p_array))


def benjamini_hochberg_thresholds(total_tests: int, q_level: float) -> np.ndarray:
    """Return BH decision thresholds k/m * q for k=1..m."""
    if total_tests <= 0:
        raise ValueError("total_tests must be positive")
    if not (0.0 < q_level <= 1.0):
        raise ValueError("q_level must be in (0, 1]")
    ranks = np.arange(1, total_tests + 1, dtype=float)
    return ranks / float(total_tests) * q_level
