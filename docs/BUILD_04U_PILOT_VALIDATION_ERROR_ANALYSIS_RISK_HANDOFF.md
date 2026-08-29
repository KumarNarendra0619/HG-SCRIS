# BUILD-04U — Pilot Results QA, Independent Validation, Error Analysis & Evidence-to-Risk Handoff

## Status
VALIDATION + HANDOFF CONTRACT LOCKED

## Purpose
Establish the quality-control gate between reconstructed historical events and downstream hazard/exposure/vulnerability/risk analysis. BUILD-04U does not merely ask whether a reconstruction "looks good"; it quantifies error where reference data permit, separates validation from calibration, diagnoses spatial/temporal/systematic error, records uncertainty, and defines exactly which reconstruction products are eligible for downstream risk modelling.

## 1. Core principle

```text
RECONSTRUCTION
      ↓
QA
      ↓
VALIDATION
      ↓
ERROR ANALYSIS
      ↓
CALIBRATION / REVISION
      ↓
REVALIDATION
      ↓
RISK-HANDOFF GATE
```

A reconstruction that fails validation is not silently passed into risk modelling.

## 2. Validation layers

Validation must distinguish:

```text
1. Structural QA
2. Internal consistency
3. Cross-source consistency
4. Spatial validation
5. Temporal validation
6. Quantitative reference validation
7. Independent validation
8. Expert review
```

Not every event will support every layer. Missing validation must be explicitly recorded rather than represented as success.

## 3. Structural QA

Check:

```text
schema completeness
geometry validity
CRS consistency
temporal field validity
unit consistency
required provenance
input/output linkage
checksum integrity
```

Structural QA failure blocks certification.

## 4. Internal consistency

Test whether the reconstruction is logically consistent with its own evidence and process representation.

Examples:

```text
process chronology
spatial continuity
parent/child process relationships
timeline ordering
parameter consistency
state consistency
```

Internal consistency is not independent validation.

## 5. Cross-source consistency

Compare independent or partially independent evidence classes while recording source dependence.

Examples:

```text
satellite interpretation ↔ field observation
meteorological timing ↔ reported onset
terrain constraint ↔ reconstructed footprint
official report ↔ geospatial evidence
```

Agreement is not treated as proof when sources share a common upstream source.

## 6. Quantitative validation metrics

Where suitable reference data exist, metrics may include:

```text
MAE
RMSE
bias / mean error
median absolute error
correlation where appropriate
precision / recall / F1 for classified footprints
intersection-over-union for spatial footprints
Hausdorff or boundary distance where appropriate
temporal onset error
peak-time error
area/volume bias
```

Metric selection is method- and variable-specific. Do not report a metric merely because it is available.

## 7. Spatial error analysis

Spatial error should be decomposed where possible:

```text
location error
boundary error
area error
omission
commission
clustered error
terrain/elevation-related error
land-cover-related error
```

Maps of residuals/error surfaces should be retained as QA products when applicable.

## 8. Temporal error analysis

Assess:

```text
onset error
duration error
peak timing error
process-transition error
sequence inversion
```

If only an interval is defensible, validation must compare interval overlap rather than inventing an exact timestamp.

## 9. Systematic error diagnosis

The analysis must distinguish:

```text
random error
systematic bias
source-specific bias
method-specific bias
scale mismatch
resolution mismatch
classification error
sampling limitation
```

A good aggregate metric must not hide a geographically or process-specific failure.

## 10. Calibration policy

Calibration may adjust registered method parameters only when scientifically justified.

```text
CALIBRATION DATA
      ↓
PARAMETER UPDATE
      ↓
NEW METHOD/RUN VERSION
      ↓
INDEPENDENT REVALIDATION
```

A calibrated result must never be validated against the same information used to calibrate it and then labelled independently validated.

## 11. No-data and weak-reference policy

If quantitative ground truth is unavailable:

```text
Do not fabricate reference values.
Do not convert expert opinion into numeric truth without method justification.
Use qualitative/interval validation where defensible.
Declare the limitation.
Reduce certification scope if necessary.
```

## 12. Confidence recalibration

Post-validation confidence must be traceable to validation evidence.

Store:

```text
pre-validation confidence
validation evidence
observed error
post-validation confidence
confidence method/version
```

Confidence should not simply increase because the model produced a plausible-looking map.

## 13. Uncertainty update

Where validation reveals additional uncertainty:

```text
Original uncertainty
       ↓
Validation findings
       ↓
Updated uncertainty
```

The updated uncertainty is versioned and linked to the evidence that caused the change.

## 14. Error register

Each material error may be represented as:

```text
error_id
run_id
output_id
error_type
location/time scope
magnitude or class
reference source
likely cause
severity
corrective_action
status
```

Errors remain auditable after correction.

## 15. Revision loop

```text
Validation finding
       ↓
Error diagnosis
       ↓
Correction decision
       ↓
New method/parameter/reconstruction version
       ↓
Re-run
       ↓
Re-validation
```

No direct editing of certified scientific outputs.

## 16. Risk-handoff principle

A reconstructed event is not automatically a hazard layer suitable for risk analysis.

Handoff requires explicit semantic mapping:

```text
RECONSTRUCTED PROCESS
        ↓
HAZARD REPRESENTATION
        ↓
EXPOSURE INTERSECTION
        ↓
VULNERABILITY
        ↓
RISK
```

Each transition is a new analytical operation with its own provenance.

## 17. Handoff eligibility classes

```text
BLOCKED
REVIEW_ONLY
EXPLORATORY
MODELLING_ELIGIBLE
RESEARCH_READY
```

A result may be `RESEARCH_READY` for reconstruction purposes but only `REVIEW_ONLY` for a particular downstream risk model if hazard semantics or uncertainty are insufficient.

## 18. Hazard handoff descriptor

Minimum fields:

```text
hazard_candidate_id
source_reconstruction_id
process_type
hazard_variable
unit
spatial_representation
temporal_representation
value_definition
uncertainty_ref
validation_ref
applicability_scope
limitations
handoff_status
```

## 19. Uncertainty propagation contract

Downstream risk models must receive uncertainty metadata rather than only point estimates where feasible.

```text
reconstruction uncertainty
        ↓
hazard uncertainty
        ↓
exposure uncertainty
        ↓
vulnerability uncertainty
        ↓
risk uncertainty
```

Propagation method is declared by the receiving analytical model.

## 20. Handoff rejection conditions

Do not hand off to operational/research risk computation when:

```text
critical validation failure
unresolved semantic mismatch
unknown spatial reference
unknown temporal reference where essential
critical provenance gap
unsupported hazard variable
unquantified critical uncertainty
method outside applicability domain
```

Exploratory use may still be allowed only when explicitly labelled.

## 21. First pilot QA report

The pilot package must contain:

```text
validation matrix
metric results
spatial error analysis
temporal error analysis
error register
calibration history
revalidation results
uncertainty update
limitations
expert-review outcome
risk-handoff decision
```

## 22. Acceptance decision matrix

```text
PASS
PASS_WITH_LIMITATIONS
REVISION_REQUIRED
REJECTED
```

Decision is based on predefined criteria, not visual plausibility or researcher preference.

## 23. Research-ready reconstruction gate

A reconstruction may enter `RESEARCH_READY` only if:

```text
structural QA passed
AND
critical validation completed
AND
errors assessed
AND
limitations documented
AND
uncertainty recorded
AND
provenance complete
AND
required expert review completed
```

Where independent quantitative validation is impossible, the certification statement must explicitly state the validation limitation and scope.

## 24. Risk handoff gate

The reconstruction can enter downstream hazard/risk modelling only if:

```text
research-ready or explicitly exploratory
AND
hazard semantics defined
AND
spatial/temporal representation defined
AND
uncertainty available or limitation documented
AND
provenance complete
AND
receiving model accepts the representation
```

## 25. Acceptance tests

```text
structural QA test
internal consistency test
spatial validation test
temporal validation test
metric calculation test
independent-validation classification test
calibration leakage test
error-register test
revision/version test
uncertainty propagation test
handoff eligibility test
blocked-handoff test
provenance test
```

## 26. BUILD-04U acceptance criteria

BUILD-04U is accepted when:

- pilot validation layers are operational;
- quantitative metrics are method-appropriate;
- spatial and temporal errors can be diagnosed;
- systematic and random error are distinguished where possible;
- calibration is separated from independent validation;
- errors are versioned and auditable;
- uncertainty can be updated after validation;
- reconstruction outputs receive explicit acceptance states;
- hazard handoff has a canonical descriptor;
- risk handoff has explicit eligibility gates;
- critical failures block silent downstream use;
- the first pilot produces a reproducible validation and handoff package.

## Next step

BUILD-04V — Hazard Engine Adapter, Reconstruction-to-Hazard Transformation & First Validated Hazard Surface.
