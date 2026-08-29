"""Canonical schemas used by HG-SCRIS ingestion pipelines."""

GLACIER_REQUIRED_FIELDS = [
    "glacier_id",
    "glacier_name",
    "rgi_id",
    "area_km2",
    "elevation_min_m",
    "elevation_max_m",
    "elevation_mean_m",
    "geometry",
]

PROVENANCE_REQUIRED_FIELDS = [
    "dataset_id",
    "dataset_version",
    "source",
    "acquisition_date",
    "processing_date",
    "method_id",
    "code_version",
    "confidence",
]
