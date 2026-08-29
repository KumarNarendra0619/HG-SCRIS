# Data directory

This directory defines the HG-SCRIS data lifecycle.

- `raw/` — immutable source downloads or source references
- `interim/` — intermediate processing products
- `processed/` — standardized datasets ready for analysis
- `derived/` — model-derived datasets
- `validation/` — validation/reference datasets

Large datasets should not be committed to GitHub. Store source metadata, checksums, scripts and lightweight samples instead.
