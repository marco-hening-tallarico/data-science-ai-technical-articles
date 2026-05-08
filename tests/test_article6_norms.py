"""Tests for Article 6 norm utilities."""

import importlib.util
from pathlib import Path

import numpy as np

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "articles"
    / "point-to-l-infinity"
    / "src"
    / "norms.py"
)
SPEC = importlib.util.spec_from_file_location("norms", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_lp_norm_and_l_infinity_consistency() -> None:
    vector_values = np.array([3.0, -4.0])
    assert np.isclose(MODULE.lp_norm(vector_values, 2), 5.0)
    assert np.isclose(MODULE.l_infinity_norm(vector_values), 4.0)


def test_regularization_penalties_are_nonnegative() -> None:
    weight_values = np.array([1.0, -2.0, 3.0])
    assert MODULE.lasso_penalty(weight_values, alpha_value=0.1) >= 0.0
    assert MODULE.ridge_penalty(weight_values, alpha_value=0.1) >= 0.0
