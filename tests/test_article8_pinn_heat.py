"""Tests for Article 8 PINN helper module."""

import importlib.util
from pathlib import Path

import numpy as np

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "articles"
    / "physics-informed-neural-networks"
    / "src"
    / "pinn_heat.py"
)
SPEC = importlib.util.spec_from_file_location("pinn_heat", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_generate_heat_solution_shapes() -> None:
    result = MODULE.generate_heat_solution(
        rod_length=1.0,
        total_time=1.0,
        spatial_points=11,
        time_steps=21,
        thermal_diffusivity=0.01,
        source_strength=1.0,
    )
    assert result["temperature_grid"].shape == (21, 11)
    assert len(result["x_coords"]) == 11
    assert len(result["t_coords"]) == 21


def test_generate_heat_solution_boundary_conditions() -> None:
    result = MODULE.generate_heat_solution(
        rod_length=1.0,
        total_time=0.2,
        spatial_points=9,
        time_steps=8,
        thermal_diffusivity=0.01,
        source_strength=1.0,
    )
    grid = result["temperature_grid"]
    assert np.allclose(grid[:, 0], 0.0)
    assert np.allclose(grid[:, -1], 0.0)
