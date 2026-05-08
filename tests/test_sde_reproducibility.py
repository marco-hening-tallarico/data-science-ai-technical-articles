"""Reproducibility checks for simple SDE simulation logic."""

import numpy as np


def simulate_ou_step(
    state_value: float, theta: float, mu: float, sigma: float, delta_t: float, seed: int
) -> float:
    """Return one seeded Euler-Maruyama step for OU process."""
    rng = np.random.default_rng(seed)
    noise = rng.normal()
    return state_value + theta * (mu - state_value) * delta_t + sigma * np.sqrt(delta_t) * noise


def test_ou_step_is_reproducible_with_seed() -> None:
    first = simulate_ou_step(0.0, 0.5, 0.0, 0.1, 0.01, seed=42)
    second = simulate_ou_step(0.0, 0.5, 0.0, 0.1, 0.01, seed=42)
    assert first == second
