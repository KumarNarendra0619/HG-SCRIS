# RGI Ingestion Specification — BUILD-01D

## Baseline
RGI 7.x is the baseline glacier inventory. The exact downloaded product/version must be recorded in provenance before processing.

## Canonical fields

- `glacier_id`
- `rgi_id`
- `glacier_name`
- `area_km2`
- `elevation_min_m`
- `elevation_max_m`
- `elevation_mean_m`
- `geometry`

## QA gates

1. CRS must be present.
2. Geometry must not be empty.
3. Geometry must be valid.
4. Glacier IDs must be checked for duplicates.
5. Area must be numeric and positive when supplied.
6. Minimum elevation must not exceed maximum elevation.
7. Mean elevation, when supplied, must fall within the min/max range.
8. Missing source attributes are retained as missing; this adapter does not invent values.

## Scientific rule
RGI baseline geometry and attributes are inventory observations/products, not direct measurements of present-day glacier state. Current-state and change analyses require additional dated observations.
