"""Article 3 helpers for NASA Pt. 1 data workflow."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from shared.nasa.data_access import fetch_power_daily_point, power_json_to_frame


def download_single_location_frame(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
    parameter_names: list[str],
) -> pd.DataFrame:
    """Fetch and convert NASA POWER daily data for one location."""
    payload = fetch_power_daily_point(
        latitude=latitude,
        longitude=longitude,
        start_date=start_date,
        end_date=end_date,
        parameters=parameter_names,
    )
    return power_json_to_frame(payload)


def save_climate_frame(climate_frame: pd.DataFrame, output_path: Path) -> None:
    """Persist climate frame to CSV with parent directory creation."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    climate_frame.to_csv(output_path, index=False)
