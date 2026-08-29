"""HG-SCRIS BUILD-04C deterministic ingestion/QA primitives.

Validation only: no silent repair, imputation, reprojection, or scientific
inference is performed here.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable, Mapping
import json


@dataclass
class QACheck:
    check_id: str
    status: str
    message: str
    details: dict[str, Any] | None = None


def check_required_columns(columns: Iterable[str], required: Iterable[str]) -> QACheck:
    missing = sorted(set(required) - set(columns))
    return QACheck("SCHEMA_REQUIRED_COLUMNS", "FAIL", "Required columns are missing", {"missing": missing}) if missing else QACheck("SCHEMA_REQUIRED_COLUMNS", "PASS", "All required columns are present")


def check_unique_ids(values: Iterable[Any], field_name: str = "id") -> QACheck:
    vals = list(values)
    non_null = [v for v in vals if v is not None and str(v).strip() != ""]
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in non_null:
        key = str(value)
        if key in seen:
            duplicates.add(key)
        seen.add(key)
    if len(non_null) != len(vals):
        return QACheck("ID_COMPLETENESS", "FAIL", f"Null/blank values found in {field_name}")
    if duplicates:
        return QACheck("ID_UNIQUENESS", "FAIL", f"Duplicate values found in {field_name}", {"duplicates": sorted(duplicates)})
    return QACheck("ID_UNIQUENESS", "PASS", f"{field_name} is complete and unique")


def check_allowed_values(values: Iterable[Any], allowed: Iterable[Any], field_name: str) -> QACheck:
    allowed_set = set(allowed)
    invalid = sorted({str(v) for v in values if v not in allowed_set})
    return QACheck("DOMAIN_VALUES", "FAIL", f"Invalid domain values in {field_name}", {"invalid": invalid}) if invalid else QACheck("DOMAIN_VALUES", "PASS", f"{field_name} contains only allowed values")


def check_file_exists(path: str | Path) -> QACheck:
    p = Path(path)
    if not p.exists():
        return QACheck("SOURCE_EXISTS", "FAIL", "Source file does not exist", {"path": str(p)})
    return QACheck("SOURCE_EXISTS", "PASS", "Source file exists", {"path": str(p), "bytes": p.stat().st_size})


def check_dataset_metadata(metadata: Mapping[str, Any]) -> list[QACheck]:
    """Validate metadata required by the real-data ingestion contract."""
    checks: list[QACheck] = []
    required = ["crs", "source_id", "source_version", "provenance", "processing_date"]
    missing = [k for k in required if metadata.get(k) in (None, "")]
    checks.append(QACheck("METADATA_REQUIRED", "FAIL" if missing else "PASS", "Required dataset metadata is missing" if missing else "Required dataset metadata is present", {"missing": missing} if missing else None))

    crs = metadata.get("crs")
    checks.append(QACheck("CRS_PRESENT", "PASS" if crs else "FAIL", "CRS is declared" if crs else "CRS is missing", {"crs": crs} if crs else None))

    provenance = metadata.get("provenance")
    prov_required = ["dataset_id", "dataset_version", "method_id", "code_version"]
    if isinstance(provenance, Mapping):
        missing_prov = [k for k in prov_required if provenance.get(k) in (None, "")]
        checks.append(QACheck("PROVENANCE_COMPLETENESS", "FAIL" if missing_prov else "PASS", "Provenance fields are missing" if missing_prov else "Core provenance fields are present", {"missing": missing_prov} if missing_prov else None))
    else:
        checks.append(QACheck("PROVENANCE_COMPLETENESS", "FAIL", "Provenance must be a mapping"))
    return checks


def check_spatial_metadata(metadata: Mapping[str, Any]) -> list[QACheck]:
    """Check spatial metadata without pretending to validate binary geometry."""
    checks: list[QACheck] = []
    if metadata.get("geometry_type"):
        checks.append(QACheck("GEOMETRY_TYPE", "PASS", "Geometry type is declared", {"geometry_type": metadata["geometry_type"]}))
    else:
        checks.append(QACheck("GEOMETRY_TYPE", "FAIL", "Geometry type is missing"))
    if metadata.get("spatial_resolution") not in (None, ""):
        checks.append(QACheck("SPATIAL_RESOLUTION", "PASS", "Spatial resolution/support is declared", {"spatial_resolution": metadata["spatial_resolution"]}))
    else:
        checks.append(QACheck("SPATIAL_RESOLUTION", "WARN", "Spatial resolution/support is not declared"))
    return checks


def write_qa_report(checks: Iterable[QACheck], output: str | Path) -> Path:
    checks = list(checks)
    report = {
        "schema_version": "04C.2",
        "status": "PASS" if all(c.status == "PASS" for c in checks) else "FAIL",
        "checks": [asdict(c) for c in checks],
    }
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return out
