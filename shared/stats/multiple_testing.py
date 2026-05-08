"""Utilities for multiple-testing corrections."""

from __future__ import annotations

import numpy as np


def bonferroni_adjust(p_values: list[float] | np.ndarray) -> np.ndarray:
    """Return Bonferroni-adjusted p-values clipped to [0, 1]."""
    p_array = np.array(p_values, dtype=float)
    return np.minimum(1.0, p_array * len(p_array))
