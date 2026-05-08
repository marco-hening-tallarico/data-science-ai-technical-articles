"""Norm and regularization helpers for Article 6."""

from __future__ import annotations

import numpy as np


def lp_norm(vector_values: np.ndarray, p_value: float) -> float:
    """Return Lp norm for p >= 1."""
    if p_value < 1:
        raise ValueError("p_value must be >= 1")
    vector_array = np.asarray(vector_values, dtype=float)
    return float(np.sum(np.abs(vector_array) ** p_value) ** (1.0 / p_value))


def l_infinity_norm(vector_values: np.ndarray) -> float:
    """Return L-infinity norm (max absolute coordinate)."""
    vector_array = np.asarray(vector_values, dtype=float)
    return float(np.max(np.abs(vector_array)))


def lasso_penalty(weight_values: np.ndarray, alpha_value: float) -> float:
    """Return L1 regularization penalty term alpha * ||w||_1."""
    return float(alpha_value * np.sum(np.abs(np.asarray(weight_values, dtype=float))))


def ridge_penalty(weight_values: np.ndarray, alpha_value: float) -> float:
    """Return L2 regularization penalty term alpha * ||w||_2^2."""
    weight_array = np.asarray(weight_values, dtype=float)
    return float(alpha_value * np.sum(weight_array**2))
