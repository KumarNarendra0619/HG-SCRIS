# BUILD-04W — Exposure Engine Adapter, Hazard–Exposure Intersection & First Validated Exposure Layer

## Status
EXPOSURE ENGINE CONTRACT LOCKED

## Purpose
Transform validated hazard products into explicit, versioned exposure information by intersecting hazard representations with population, settlement, building, infrastructure, environmental and other relevant asset inventories. BUILD-04W separates exposure from vulnerability: an exposed asset is not automatically a vulnerable asset and exposure is not automatically risk.

## 1. Core scientific chain

```text
VALIDATED HAZARD
      ↓
EXPOSURE DEFINITION
      ↓
ASSET/POPULATION INVENTORY
      ↓
SPATIAL + TEMPORAL ALIGNMENT
      ↓
HAZARD–EXPOSURE INTERSECTION
      ↓
EXPOSURE QUANTIFICATION
      ↓
UNCERTAINTY / DATA QUALITY
      ↓
VALIDATED EXPOSURE LAYER
      ↓
VULNERABILITY HANDOFF
```

## 2. Exposure definition

Every exposure product declares:

```text
exposure_id
hazard_id
asset_class
asset_variable
unit
reference_time
spatial_representation
population/asset definition
aggregation level
inventory version
method_id
method_version
```

The term `exposure` must not be used without defining what is exposed and to which hazard state/time.

## 3. Asset classes

Support typed inventories:

```text
population
households
settlements
buildings
roads
bridges
schools
health facilities
water infrastructure
power/utility assets
agricultural land/crops
livestock
critical facilities
ecosystem/environmental assets
other registered assets
```

The engine is extensible; unsupported asset semantics must not be inferred automatically.

## 4. Population exposure

Population exposure may be represented as:

```text
people exposed
households exposed
population density exposed
age/sex groups exposed
social groups exposed where ethically and scientifically justified
```

Demographic attributes must retain their census/survey/reference year and spatial support.

Population counts must not be interpreted as real-time population unless the data support that claim.

## 5. Asset inventory contract

Each inventory declares:

```text
inventory_id
inventory_version
asset_id
asset_class
geometry
geometry_precision
reference_date
attributes
source
source_version
quality
license/access
```

Original inventories remain immutable. Derived exposure records reference the exact inventory version used.

## 6. Spatial alignment

Supported operations:

```text
point-in-polygon
line-hazard intersection
polygon overlay
raster zonal statistics
distance/buffer intersection
grid-to-grid alignment
network segment intersection
```

All transformations record CRS, target resolution, geometry processing and parameters.

## 7. Hazard semantics must be preserved

Exposure calculation depends on hazard representation:

```text
binary extent
→ exposed/not exposed

categorical severity
→ exposure by severity class

continuous intensity
→ exposure by intensity threshold/range/statistics

arrival time
→ exposure within time window

duration
→ exposure-duration metric
```

The engine must not treat every hazard as a binary mask.

## 8. Temporal exposure

Exposure can be time-dependent:

```text
population at event time
asset status at event time
seasonal agricultural exposure
infrastructure availability
pre/post-event exposure state
```

Reference date/time must be retained. Temporal mismatch is reported rather than silently ignored.

## 9. Dasymetric / spatial disaggregation safeguard

Where population or asset data are aggregated, spatial disaggregation may be used only through a registered method.

```text
coarse population
      ↓
registered spatial allocation model
      ↓
fine exposure estimate
```

The output must be labelled estimated/disaggregated and must retain the allocation assumptions.

## 10. Exposure calculation modes

Support:

```text
binary exposure count
weighted exposure
area exposed
asset count exposed
length exposed
population-weighted hazard statistics
threshold exceedance
exposure by hazard class
exposure time/duration
```

The calculation definition and denominator must always be explicit.

## 11. Uncertainty

Exposure uncertainty may arise from:

```text
hazard uncertainty
asset-location uncertainty
inventory completeness
population estimation
spatial disaggregation
temporal mismatch
classification uncertainty
```

Store component uncertainties where feasible and retain source quality indicators.

## 12. Hazard uncertainty propagation

```text
Hazard estimate + uncertainty
             ↓
Exposure intersection
             ↓
Exposure estimate + uncertainty descriptor
```

Deterministic, interval, ensemble, probabilistic or sensitivity approaches must be declared by the selected method.

## 13. Exposure quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
VALIDATION_PENDING
VALIDATED_WITH_LIMITATIONS
RESEARCH_READY
SUPERSEDED
REJECTED
```

## 14. Exposure validation

Possible validation sources include:

```text
independent asset inventory
field verification
official facility lists
independent population estimates
high-resolution imagery
post-event assessment records
```

Validation evidence must be classified separately from the inventory used to construct the exposure layer.

## 15. Quantitative validation

Depending on the exposure variable:

```text
counts → absolute/relative error
continuous exposure → MAE/RMSE/bias
classification → precision/recall/F1/confusion matrix
spatial asset locations → positional error
line exposure → length error
area exposure → area difference/IoU where appropriate
```

Metrics must match the measurement scale.

## 16. Missing/incomplete inventory policy

The engine must distinguish:

```text
zero exposure
no observed asset
unknown exposure
missing inventory
outside coverage
```

These states must never be collapsed into a single zero value.

## 17. Exposure denominator discipline

Report both numerator and denominator where applicable:

```text
exposed population / total population
exposed buildings / inventory buildings
exposed road length / mapped road length
```

Unknown or uncovered assets must not be silently included in the denominator.

## 18. Exposure aggregation

Support aggregation by:

```text
place
administrative unit
hazard class
asset class
settlement
watershed/catchment
road segment
grid cell
demographic category
```

Aggregation must preserve the source spatial support and uncertainty.

## 19. First validated exposure layer

The first pilot output should be bounded:

```text
ONE validated hazard
      ↓
ONE registered asset/population inventory
      ↓
ONE exposure variable
      ↓
ONE spatial/temporal domain
      ↓
VALIDATION
      ↓
FIRST VALIDATED EXPOSURE LAYER
```

Do not create a pseudo-comprehensive exposure database without verified inventories.

## 20. Exposure engine adapter

The adapter follows the common execution contract:

```text
validate_inputs()
execute()
validate_outputs()
health()
```

Input:

```text
run_id
hazard_refs[]
inventory_refs[]
exposure_definition
method_id
method_version
spatial/temporal parameters
uncertainty policy
```

Output:

```text
exposure_id
run_id
exposure_definition
artifact_refs[]
validation_refs[]
uncertainty_ref
coverage
quality_state
handoff_status
```

## 21. Exposure-to-vulnerability handoff

Exposure is not vulnerability.

```text
EXPOSURE
  ↓
VULNERABILITY MODEL
  ↓
SUSCEPTIBILITY / COPING / ADAPTIVE CAPACITY
  ↓
RISK
```

The handoff descriptor must contain enough semantics for the vulnerability model to interpret the exposed unit correctly.

## 22. Handoff descriptor

```text
exposure_id
hazard_id
asset_class
exposure_variable
unit
spatial_support
temporal_support
inventory_version
uncertainty_ref
validation_ref
coverage
limitations
handoff_status
```

## 23. Handoff eligibility

```text
BLOCKED
REVIEW_ONLY
EXPLORATORY
MODELLING_ELIGIBLE
RESEARCH_READY
```

A layer may be research-ready for one exposure variable but unsuitable for another downstream vulnerability model.

## 24. Stop conditions

Block or downgrade when:

```text
hazard semantics unresolved
inventory version unresolved
critical spatial mismatch
critical temporal mismatch
coverage unknown
asset definition ambiguous
critical inventory completeness problem
provenance gap
unsupported exposure calculation
uncertainty unavailable where essential
```

## 25. Reproducibility manifest

Record:

```text
exposure run ID
hazard version
inventory versions
method/version
parameters
CRS/grid
reference time
code/environment
input checksums
output checksums
validation results
uncertainty record
coverage assessment
review state
```

## 26. Acceptance tests

```text
hazard compatibility test
inventory schema test
CRS alignment test
temporal alignment test
point/polygon intersection test
line intersection test
raster zonal-statistics test
extent-vs-intensity semantic test
disaggregation labelling test
missing-vs-zero exposure test
denominator test
uncertainty retention test
validation classification test
provenance test
handoff eligibility test
blocked-handoff test
reproducibility test
```

## 27. Acceptance criteria

BUILD-04W is accepted when:

- exposure is explicitly separated from vulnerability;
- typed population/asset inventories are supported;
- inventory versions and reference dates are frozen per run;
- hazard semantics determine the exposure calculation;
- spatial and temporal alignment are auditable;
- spatial disaggregation is method-registered and labelled;
- missing/unknown/zero exposure states are separated;
- denominators are explicit;
- uncertainty is retained;
- exposure validation is independently classified;
- exposure products have quality states;
- vulnerability handoff is semantically defined;
- critical failures block silent downstream use;
- a bounded first validated exposure layer can be produced reproducibly.

## Next step

BUILD-04X — Vulnerability Engine Adapter, Exposure-to-Vulnerability Transformation, Social/Physical Vulnerability Profiles & First Validated Vulnerability Layer.
