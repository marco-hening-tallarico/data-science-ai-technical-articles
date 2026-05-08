"""NASA POWER API helper functions."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd
import requests


def fetch_power_daily_point(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
    parameters: Iterable[str],
    community: str = "AG",
) -> dict:
    """Fetch daily point data from NASA POWER API."""
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    query_params = {
        "parameters": ",".join(parameters),
        "community": community,
        "longitude": longitude,
        "latitude": latitude,
        "start": start_date,
        "end": end_date,
        "format": "JSON",
    }
    response = requests.get(url, params=query_params, timeout=60)
    response.raise_for_status()
    return response.json()


def power_json_to_frame(power_payload: dict) -> pd.DataFrame:
    """Convert NASA POWER JSON payload into a tidy DataFrame."""
    parameter_map = power_payload["properties"]["parameter"]
    climate_frame = pd.DataFrame(parameter_map)
    climate_frame.index = pd.to_datetime(climate_frame.index, format="%Y%m%d")
    climate_frame = climate_frame.reset_index().rename(columns={"index": "date"})
    return climate_frame
