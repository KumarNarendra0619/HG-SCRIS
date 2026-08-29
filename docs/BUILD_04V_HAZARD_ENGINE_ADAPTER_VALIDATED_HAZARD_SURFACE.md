# BUILD-04V — Hazard Engine Adapter, Reconstruction-to-Hazard Transformation & First Validated Hazard Surface

## Status
HAZARD TRANSFORMATION + ENGINE CONTRACT LOCKED

## Purpose
Convert validated reconstruction products into explicit hazard representations suitable for downstream exposure, vulnerability and risk analysis. BUILD-04V does not equate a reconstructed process footprint with a complete hazard model. It requires a declared hazard variable, process semantics, temporal/spatial representation, uncertainty treatment, validation evidence and applicability domain.

## 1. Core scientific chain

```text
VALIDATED RECONSTRUCTION
        ↓
PROCESS SEMANTICS
        ↓
HAZARD DEFINITION
        ↓
HAZARD TRANSFORMATION / MODELLING
        ↓
VALIDATION
        ↓
UNCERTAINTY
        ↓
VALIDATED HAZARD SURFACE
        ↓
EXPOSURE HANDOFF
```

A footprint is not automatically a hazard intensity surface. If only occurrence/extent is defensible, the output must remain an extent/occurrence product.

## 2. Hazard representation classes

Support explicit classes:

```text
occurrence / binary extent
categorical severity
continuous intensity
frequency / rate
probability
arrival time
duration
depth / height
velocity
pressure / load
compound hazard state
```

Only representations supported by the evidence and registered method may be produced.

## 3. Hazard definition contract

Every hazard product declares:

```text
hazard_id
source_reconstruction_id
hazard_type
process_type
variable
unit
value_definition
spatial_resolution
spatial_reference
temporal_reference
valid_time_window
applicability_domain
method_id
method_version
```

No ambiguous layer named simply `hazard` is permitted in the research registry.

## 4. Transformation contract

```text
reconstruction artifact
       ↓
semantic interpretation
       ↓
registered transformation method
       ↓
hazard candidate
       ↓
QA + validation
       ↓
hazard product
```

The transformation method must be independently versioned from the reconstruction method.

## 5. Hazard engine adapter

The adapter follows BUILD-04Q:

```text
validate_inputs()
execute()
validate_outputs()
health()
```

Input contract:

```text
run_id
reconstruction_refs[]
dataset_refs[]
hazard_definition
method_id
method_version
parameter_set
spatial_grid / target geometry
temporal window
uncertainty policy
```

Output contract:

```text
hazard_id
run_id
hazard_definition
artifact_refs[]
validation_refs[]
uncertainty_ref
coverage
quality_state
handoff_status
```

## 6. Reconstruction-to-hazard decision gate

Before transformation ask:

```text
Does the reconstruction support only occurrence/extent?
OR
Does it support a physical intensity variable?
OR
Does an independently justified hazard model infer intensity?
```

If the evidence supports only extent, the system must not manufacture intensity values.

## 7. Spatial transformation

The engine may transform:

```text
vector → raster
raster → target grid
point observations → surface
process footprint → hazard mask
```

Every transformation records:

```text
source geometry
source CRS
target CRS
grid resolution
resampling/interpolation method
parameters
mask rules
```

Resolution cannot imply accuracy greater than the source evidence supports.

## 8. Temporal transformation

Hazard products may represent:

```text
instant
interval
peak period
time series
arrival time
duration
```

Temporal interpolation/extrapolation must be explicit. Unknown temporal detail remains unknown.

## 9. Intensity modelling

Where physical intensity is modelled rather than observed, the output must be labelled as modelled and include:

```text
model assumptions
boundary/initial conditions
input datasets
parameters
calibration data
validation data
model version
known limitations
```

A modelled intensity is not relabelled as observed intensity.

## 10. First validated hazard surface

The first real output should be deliberately bounded:

```text
ONE validated reconstruction
      ↓
ONE hazard variable
      ↓
ONE declared spatial/temporal domain
      ↓
ONE registered transformation/model
      ↓
VALIDATION
      ↓
FIRST VALIDATED HAZARD SURFACE
```

Do not create multiple unsupported hazard variables simply to make the platform appear complete.

## 11. Validation framework

Where reference data permit:

```text
continuous surface → MAE / RMSE / bias / appropriate correlation
binary extent → IoU / precision / recall / F1
categorical hazard → confusion matrix / class metrics
arrival time → temporal error
boundary → distance/error metrics
```

Validation metrics are selected according to the hazard variable and measurement scale.

## 12. Spatial validation

Assess:

```text
extent agreement
boundary displacement
omission/commission
hotspot displacement
terrain-dependent bias
resolution mismatch
```

A single aggregate score must not conceal critical local failure.

## 13. Uncertainty representation

Hazard output retains:

```text
source reconstruction uncertainty
transformation uncertainty
model uncertainty
parameter uncertainty
spatial uncertainty
temporal uncertainty
```

If quantitative propagation is not defensible, the product records qualitative or bounded uncertainty rather than a fabricated probability.

## 14. Hazard quality states

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

## 15. Handoff eligibility

```text
BLOCKED
REVIEW_ONLY
EXPLORATORY
MODELLING_ELIGIBLE
RESEARCH_READY
```

A validated hazard product is eligible for downstream analysis only if its semantics match the receiving exposure/risk model.

## 16. Exposure handoff descriptor

```text
hazard_id
hazard_type
hazard_variable
unit
spatial_representation
temporal_representation
validity_window
uncertainty_ref
validation_ref
applicability_domain
limitations
handoff_status
```

## 17. Hazard uncertainty propagation

The exposure engine receives the hazard uncertainty descriptor, not just the central surface.

```text
Hazard estimate + uncertainty
          ↓
Exposure intersection
          ↓
Exposure uncertainty contribution
```

The receiving model must declare whether it uses deterministic, interval, ensemble, probabilistic or sensitivity-based propagation.

## 18. Compound hazards

Compound hazards are represented explicitly:

```text
hazard A
   +
hazard B
   +
interaction rule
   ↓
compound hazard state
```

The interaction rule must be registered. Co-location alone does not establish physical interaction.

## 19. Failure/stop conditions

Transformation is blocked when:

```text
hazard variable undefined
reconstruction outside applicability domain
spatial reference unresolved
temporal window unresolved
critical uncertainty missing
validation reference unavailable where required
method/schema mismatch
provenance incomplete
```

## 20. Reproducibility manifest

Record:

```text
hazard run ID
reconstruction version
hazard method/version
input dataset versions
parameters
code/environment
spatial grid
temporal window
random seed if applicable
input checksums
output checksums
validation results
uncertainty record
review state
```

## 21. First validated surface certification

Certification requires:

```text
validated reconstruction
AND
explicit hazard definition
AND
registered transformation/model
AND
spatial/temporal semantics
AND
validation evidence
AND
uncertainty record
AND
provenance completeness
AND
limitations statement
```

## 22. Acceptance tests

```text
input reconstruction compatibility
hazard-definition validation
extent-only protection test
spatial transformation test
temporal transformation test
intensity-model labelling test
validation metric test
uncertainty retention test
compound-hazard schema test
provenance test
handoff eligibility test
blocked-handoff test
reproducibility test
```

## 23. Acceptance criteria

BUILD-04V is accepted when:

- hazard representations are explicitly typed;
- reconstruction-to-hazard semantics are separated;
- hazard transformation methods are versioned;
- the adapter follows the common execution contract;
- extent-only evidence cannot silently become intensity;
- spatial and temporal transformations are auditable;
- modelled intensity remains labelled modelled;
- uncertainty is retained;
- hazard validation is variable-appropriate;
- compound hazards have explicit interaction rules;
- handoff eligibility is enforced;
- the first bounded validated hazard surface can be produced reproducibly.

## Next step

BUILD-04W — Exposure Engine Adapter, Hazard–Exposure Intersection, Population/Asset Exposure Inventory & First Validated Exposure Layer.
