"""Utilities for Ornstein-Uhlenbeck process simulation and fitting."""

from __future__ import annotations

import numpy as np


def simulate_ou_path(
    *,
    initial_value: float,
    theta: float,
    mu: float,
    sigma: float,
    delta_t: float,
    num_steps: int,
    random_seed: int = 42,
) -> np.ndarray:
    """Simulate an OU trajectory via Euler-Maruyama discretization."""
    if num_steps <= 0:
        raise ValueError("num_steps must be positive")
    rng = np.random.default_rng(random_seed)
    path = np.empty(num_steps + 1, dtype=float)
    path[0] = initial_value
    for step_index in range(1, num_steps + 1):
        noise = rng.normal()
        previous_value = path[step_index - 1]
        drift = theta * (mu - previous_value) * delta_t
        diffusion = sigma * np.sqrt(delta_t) * noise
        path[step_index] = previous_value + drift + diffusion
    return path


def estimate_ou_mean_reversion(series_values: np.ndarray, delta_t: float) -> float:
    """Estimate rough mean-reversion speed from lag-1 autocorrelation."""
    if len(series_values) < 3:
        raise ValueError("series_values must include at least 3 points")
    centered = series_values - np.mean(series_values)
    autocov_0 = np.dot(centered, centered) / len(centered)
    autocov_1 = np.dot(centered[1:], centered[:-1]) / (len(centered) - 1)
    if autocov_0 <= 0 or autocov_1 <= 0:
        raise ValueError("autocovariance values must be positive for estimation")
    lag_correlation = autocov_1 / autocov_0
    return -np.log(lag_correlation) / delta_t
