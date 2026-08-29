# BUILD-02B — Verified Glacier Inventory & Glacier-State Baseline

## Objective
Create one canonical, provenance-aware glacier layer that can support downstream connectivity, terrain analysis, cascade modelling and risk analysis across the Himalaya.

## Important scientific rule
A glacier inventory is not a single timeless truth. Different inventories, observation dates and delineation methods can produce different boundaries. HG-SCRIS therefore preserves source identity/date/version and does not silently merge conflicting inventories.

## Canonical identity
Every source feature receives:

- source_glacier_id
- hgscris_glacier_id
- inventory_name
- inventory_version
- lineage_id

The HG-SCRIS ID is a stable platform identifier, not a claim that two geometrically similar polygons from different inventories are physically identical.

## Core attributes

- geometry
- area_km2
- minimum/mean/maximum elevation where derivable
- mean slope where derivable
- aspect where appropriate
- mass-balance value and period when available
- ice thickness when independently available
- volume when independently available
- linked lake/outlet/hydrography IDs after connectivity validation
- data quality
- uncertainty
- source/provenance

## Data hierarchy
Use authoritative scientific inventories where available; supplement with established research/global products. Different epochs should remain temporally explicit.

## Geometry QA
For each inventory:

1. validate geometry
2. detect empty/invalid polygons
3. detect duplicates/overlaps
4. verify area calculation in an appropriate projected/equal-area CRS
5. compare feature IDs and source attributes
6. record processing version

## Attribute QA

- area > 0
- elevation range internally consistent
- slope within 0–90 degrees
- units explicit
- mass-balance sign convention explicit
- missing values preserved as missing, not zero

## Glacier-state time series
Where multiple observation epochs exist, preserve a temporal table rather than overwriting the baseline:

`glacier_id + observation_date + variable + value + unit + source`

This supports area change, elevation/state change and event-before/event-after analysis.

## Mass and volume
Mass-balance, thickness and volume are not interchangeable. The system must retain the original variable, unit, period and method. Missing mass data must not be fabricated from area.

## Glacier-to-lake linkage
A lake is linked to a glacier only after spatial/temporal evidence and connectivity checks. Simple nearest-neighbour matching is not sufficient for final scientific linkage.

## Glacier-to-hydrography linkage
Downstream reach assignment should use terrain/hydrographic connectivity and be stored as a validated relationship with method/version metadata.

## Derived terrain attributes
Elevation, slope and aspect may be derived from the selected DEM, but DEM version/resolution must be stored alongside each derived attribute. Do not mix attributes generated from incompatible DEMs without documentation.

## Uncertainty
Track uncertainty from:

- inventory delineation
- imagery/resolution
- temporal mismatch
- DEM
- attribute derivation
- source conflicts

## Outputs

- canonical glacier layer
- glacier temporal-state table
- glacier QA report
- source-to-canonical crosswalk
- glacier-lake linkage table
- glacier-hydrography linkage table
- provenance manifest

## Acceptance gate
A glacier feature becomes `passed` only when identity, geometry, units, source metadata and QA checks are complete. It may remain usable for exploratory mapping as `pending`, but production modelling must distinguish the status.

## Next step
BUILD-02C — DEM/Terrain Baseline Loader and Valley Morphometry.
