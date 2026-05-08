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


def benjamini_hochberg_rejection_mask(
    p_values: list[float] | np.ndarray,
    q_level: float,
) -> np.ndarray:
    """Return boolean mask of BH discoveries at target FDR level."""
    p_array = np.array(p_values, dtype=float)
    if p_array.ndim != 1 or p_array.size == 0:
        raise ValueError("p_values must be a non-empty 1D array-like")
    if not (0.0 < q_level <= 1.0):
        raise ValueError("q_level must be in (0, 1]")

    sorted_indices = np.argsort(p_array)
    sorted_p_values = p_array[sorted_indices]
    thresholds = benjamini_hochberg_thresholds(sorted_p_values.size, q_level)
    passing = sorted_p_values <= thresholds
    if not np.any(passing):
        return np.zeros_like(p_array, dtype=bool)

    max_passing_rank = np.where(passing)[0].max()
    cutoff_value = sorted_p_values[max_passing_rank]
    return p_array <= cutoff_value
