"""Tests for Article 4 OU helper module."""

import importlib.util
from pathlib import Path

import numpy as np

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "articles"
    / "nasa-climate-data-pt2-sdes"
    / "src"
    / "sde_ou.py"
)
SPEC = importlib.util.spec_from_file_location("sde_ou", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_simulate_ou_path_seeded_reproducible() -> None:
    first_path = MODULE.simulate_ou_path(
        initial_value=0.0,
        theta=0.5,
        mu=0.0,
        sigma=0.1,
        delta_t=0.01,
        num_steps=20,
        random_seed=7,
    )
    second_path = MODULE.simulate_ou_path(
        initial_value=0.0,
        theta=0.5,
        mu=0.0,
        sigma=0.1,
        delta_t=0.01,
        num_steps=20,
        random_seed=7,
    )
    assert np.allclose(first_path, second_path)


def test_estimate_ou_mean_reversion_positive() -> None:
    series_values = np.array([0.01, 0.02, 0.021, 0.023, 0.024, 0.026])
    estimate = MODULE.estimate_ou_mean_reversion(series_values, delta_t=1.0)
    assert estimate > 0
