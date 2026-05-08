"""Helpers for PINN inverse heat-equation experiments."""

from __future__ import annotations

import random
from typing import Any

import numpy as np


def set_global_seed(random_seed: int = 42) -> None:
    """Set reproducibility seeds for available libraries."""
    random.seed(random_seed)
    np.random.seed(random_seed)

    try:
        import torch  # type: ignore

        torch.manual_seed(random_seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(random_seed)
    except Exception:
        pass

    try:
        import tensorflow as tf  # type: ignore

        tf.random.set_seed(random_seed)
    except Exception:
        pass


def generate_heat_solution(
    rod_length: float,
    total_time: float,
    spatial_points: int,
    time_steps: int,
    thermal_diffusivity: float,
    source_strength: float,
) -> dict[str, Any]:
    """Generate synthetic 1D heat-equation temperature surface."""
    x_coords = np.linspace(0.0, rod_length, spatial_points)
    t_coords = np.linspace(0.0, total_time, time_steps)
    dx = x_coords[1] - x_coords[0]
    dt = t_coords[1] - t_coords[0]

    temperature_grid = np.zeros((time_steps, spatial_points), dtype=float)
    for time_index in range(1, time_steps):
        previous = temperature_grid[time_index - 1].copy()
        current = previous.copy()
        for space_index in range(1, spatial_points - 1):
            laplace = (
                previous[space_index + 1]
                - 2.0 * previous[space_index]
                + previous[space_index - 1]
            ) / (dx**2)
            current[space_index] = previous[space_index] + dt * (
                thermal_diffusivity * laplace + source_strength
            )
        current[0] = 0.0
        current[-1] = 0.0
        temperature_grid[time_index] = current

    return {"x_coords": x_coords, "t_coords": t_coords, "temperature_grid": temperature_grid}
