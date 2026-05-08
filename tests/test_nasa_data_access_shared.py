"""Tests for shared NASA data-access helpers."""

import pandas as pd

from shared.nasa.data_access import power_json_to_frame


def test_power_json_to_frame_schema() -> None:
    payload = {
        "properties": {
            "parameter": {
                "T2M": {"20250101": 10.0, "20250102": 11.0},
                "PRECTOTCORR": {"20250101": 0.1, "20250102": 0.2},
            }
        }
    }
    frame = power_json_to_frame(payload)
    assert isinstance(frame, pd.DataFrame)
    assert "date" in frame.columns
    assert "T2M" in frame.columns
    assert "PRECTOTCORR" in frame.columns
    assert len(frame) == 2
