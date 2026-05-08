"""Tests for Article 3 NASA Pt. 1 helper functions."""

import importlib.util
from pathlib import Path

import pandas as pd

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "articles"
    / "nasa-climate-data-pt1"
    / "src"
    / "nasa_pt1_pipeline.py"
)
SPEC = importlib.util.spec_from_file_location("nasa_pt1_pipeline", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_save_climate_frame_creates_output(tmp_path: Path) -> None:
    sample_frame = pd.DataFrame({"date": ["2025-01-01"], "T2M": [20.0]})
    output_path = tmp_path / "processed" / "climate_data.csv"
    MODULE.save_climate_frame(sample_frame, output_path)
    assert output_path.exists()
    reloaded = pd.read_csv(output_path)
    assert list(reloaded.columns) == ["date", "T2M"]
