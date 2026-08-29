"""Dataset registry validation for reproducible HG-SCRIS workflows."""

from __future__ import annotations

from dataclasses import dataclass, asdict

REQUIRED_FIELDS = (
    "dataset_id", "theme", "provider", "product_or_dataset", "spatial_coverage",
    "temporal_coverage", "resolution", "crs", "vertical_datum", "access_url",
    "license", "acquisition_date", "processing_version", "qa_status"
)


@dataclass(frozen=True)
class DatasetRecord:
    dataset_id: str
    theme: str
    provider: str
    product_or_dataset: str
    spatial_coverage: str
    temporal_coverage: str
    resolution: str
    crs: str
    vertical_datum: str
    access_url: str
    license: str
    acquisition_date: str
    processing_version: str
    qa_status: str
    notes: str = ""

    def validate_identity(self) -> list[str]:
        errors = []
        for key, value in asdict(self).items():
            if key != "notes" and not str(value).strip():
                errors.append(f"Missing required field: {key}")
        if self.qa_status not in {"not_started", "pending", "passed", "failed"}:
            errors.append("qa_status must be not_started, pending, passed or failed")
        return errors


def assert_registry_headers(headers: list[str]) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in headers]
    if missing:
        raise ValueError(f"Registry missing required fields: {missing}")
