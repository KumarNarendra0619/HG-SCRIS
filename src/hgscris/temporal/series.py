"""Quality-controlled temporal series utilities."""

from __future__ import annotations

import pandas as pd

REQUIRED = {"entity_id", "observation_date", "value", "variable", "source"}


def validate_series(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and sort a temporal observation table without imputing missing data."""
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    out = df.copy()
    out["observation_date"] = pd.to_datetime(out["observation_date"], errors="raise")
    out["value"] = pd.to_numeric(out["value"], errors="raise")
    if out[["entity_id", "variable", "source"]].isna().any().any():
        raise ValueError("Entity, variable and source cannot be missing.")
    return out.sort_values(["entity_id", "variable", "observation_date"]).reset_index(drop=True)


def change_table(df: pd.DataFrame) -> pd.DataFrame:
    """Compute first-to-last absolute and relative change per entity/variable."""
    x = validate_series(df)
    rows = []
    for (entity_id, variable), g in x.groupby(["entity_id", "variable"], sort=False):
        first, last = g.iloc[0], g.iloc[-1]
        delta = float(last.value - first.value)
        relative = None if float(first.value) == 0 else delta / float(first.value)
        rows.append({
            "entity_id": entity_id,
            "variable": variable,
            "start_date": first.observation_date.date().isoformat(),
            "end_date": last.observation_date.date().isoformat(),
            "start_value": float(first.value),
            "end_value": float(last.value),
            "absolute_change": delta,
            "relative_change": relative,
            "source_start": first.source,
            "source_end": last.source,
        })
    return pd.DataFrame(rows)
