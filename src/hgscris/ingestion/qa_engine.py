"""HG-SCRIS BUILD-04C: lightweight deterministic ingestion/QA primitives.

This module intentionally performs validation and reporting only. It does not
silently repair scientific data or invent missing values.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable
import json


@dataclass
class QACheck:
    check_id: str
    status: str
    message: str
    details: dict[str, Any] | None = None


def check_required_columns(columns: Iterable[str], required: Iterable[str]) -> QACheck:
    cols = set(columns)
    missing = sorted(set(required) - cols)
    if missing:
        return QACheck("SCHEMA_REQUIRED_COLUMNS", "FAIL", "Required columns are missing", {"missing": missing})
    return QACheck("SCHEMA_REQUIRED_COLUMNS", "PASS", "All required columns are present")


def check_unique_ids(values: Iterable[Any], field_name: str = "id") -> QACheck:
    vals = list(values)
    non_null = [v for v in vals if v is not None and str(v).strip() != ""]
    duplicates = sorted({str(v) for v in non_null if non_null.count(v) > 1})
    if duplicates:
        return QACheck("ID_UNIQUENESS", "FAIL", f"Duplicate values found in {field_name}", {"duplicates": duplicates})
    if len(non_null) != len(vals):
        return QACheck("ID_COMPLETENESS", "FAIL", f"Null/blank values found in {field_name}")
    return QACheck("ID_UNIQUENESS", "PASS", f"{field_name} is complete and unique")


def check_allowed_values(values: Iterable[Any], allowed: Iterable[Any], field_name: str) -> QACheck:
    allowed_set = set(allowed)
    invalid = sorted({str(v) for v in values if v not in allowed_set})
    if invalid:
        return QACheck("DOMAIN_VALUES", "FAIL", f"Invalid domain values in {field_name}", {"invalid": invalid})
    return QACheck("DOMAIN_VALUES", "PASS", f"{field_name} contains only allowed values")


def check_file_exists(path: str | Path) -> QACheck:
    p = Path(path)
    if not p.exists():
        return QACheck("SOURCE_EXISTS", "FAIL", "Source file does not exist", {"path": str(p)})
    return QACheck("SOURCE_EXISTS", "PASS", "Source file exists", {"path": str(p), "bytes": p.stat().st_size})


def write_qa_report(checks: Iterable[QACheck], output: str | Path) -> Path:
    checks = list(checks)
    report = {
        "schema_version": "04C.1",
        "status": "PASS" if all(c.status == "PASS" for c in checks) else "FAIL",
        "checks": [asdict(c) for c in checks],
    }
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return out
