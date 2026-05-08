"""Smoke tests for NASA preprocessing conventions."""

import pandas as pd

from shared.nasa.preprocessing import normalize_nasa_columns


def test_normalize_nasa_columns() -> None:
    input_frame = pd.DataFrame({"Temperature Max": [1.0], "Date ": ["2025-01-01"]})
    output_frame = normalize_nasa_columns(input_frame)
    assert "temperature_max" in output_frame.columns
    assert "date" in output_frame.columns
