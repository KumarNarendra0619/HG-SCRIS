# BUILD-04Z — Cross-Stage Scientific QA, End-to-End Provenance Audit, Uncertainty Audit & Pilot Certification

## Status
CROSS-STAGE CERTIFICATION GATE LOCKED

## Purpose
BUILD-04Z is the final scientific gate for the 04-series. It audits the complete chain from real evidence and event reconstruction through hazard, exposure, vulnerability and risk. It does not manufacture a pass result. It determines whether a pilot is scientifically reproducible, traceable, valid for its stated purpose and eligible for the HG-SCRIS v1.0 research-ready state.

## 1. End-to-end chain

```text
REAL EVIDENCE
   ↓
RECONSTRUCTION
   ↓
VALIDATION
   ↓
HAZARD
   ↓
EXPOSURE
   ↓
VULNERABILITY
   ↓
RISK
   ↓
CROSS-STAGE QA
   ↓
CERTIFICATION
```

Every downstream artifact must reference the exact upstream version used.

## 2. Certification principle

```text
QUALITY ≠ COMPLETENESS

RESEARCH-READY ≠ PERFECT

VALIDATED ≠ UNIVERSALLY VALID
```

Certification is conditional on declared scope, evidence, method and applicability domain.

## 3. Cross-stage audit matrix

Audit each stage for:

```text
identity
provenance
semantics
spatial reference
temporal reference
units
coverage
data quality
method/version
parameters
uncertainty
validation
limitations
handoff state
```

Stages:

```text
04T Evidence
04U Validation
04V Hazard
04W Exposure
04X Vulnerability
04Y Risk
```

## 4. Lineage audit

Required lineage:

```text
source evidence
   ↓
source version/checksum
   ↓
reconstruction run/version
   ↓
validation record
   ↓
hazard run/version
   ↓
exposure run/version
   ↓
vulnerability run/version
   ↓
risk run/version
```

Any broken critical lineage produces a certification downgrade or block.

## 5. Semantic consistency audit

Verify that terminology remains stable across stages:

```text
hazard ≠ exposure
exposure ≠ vulnerability
vulnerability ≠ risk
reconstruction ≠ hazard intensity
normalized index ≠ physical loss
modelled value ≠ observed value
```

A semantic mismatch is a critical finding when it changes interpretation.

## 6. Spatial audit

Check:

```text
CRS
coordinate units
source geometry
spatial resolution
spatial support
alignment
resampling/interpolation
boundary handling
positional uncertainty
aggregation/disaggregation
```

Detect false precision caused by finer output grids than the evidence supports.

## 7. Temporal audit

Check:

```text
event date/time
reference period
observation period
inventory date
vulnerability reference year
risk scenario period
lags
interpolation/extrapolation
```

Historical evidence must not silently become a current-state claim.

## 8. Unit and scale audit

For every quantitative variable verify:

```text
variable name
unit
scale/range
normalization
meaning of zero
meaning of one
transformation
aggregation
```

No multiplication, addition or thresholding of incompatible quantities is permitted.

## 9. Uncertainty audit

Trace uncertainty through:

```text
Evidence
 ↓
Reconstruction uncertainty
 ↓
Hazard uncertainty
 ↓
Exposure uncertainty
 ↓
Vulnerability uncertainty
 ↓
Risk uncertainty
```

Audit whether uncertainty was:

```text
retained
quantified where defensible
bounded where appropriate
described qualitatively where necessary
silently discarded
```

Silent loss of material uncertainty is a certification finding.

## 10. Validation independence audit

For every validation claim ask:

```text
Was the reference data used for calibration?
Was it used to tune parameters?
Was it used for model selection?
Is it genuinely independent?
Is independence only partial?
```

Labels:

```text
INDEPENDENT
PARTIALLY INDEPENDENT
CALIBRATION-BASED
INTERNAL ONLY
UNKNOWN
```

Unknown independence cannot be reported as independent validation.

## 11. Error propagation audit

Trace known errors:

```text
source error
 ↓
reconstruction error
 ↓
hazard error
 ↓
exposure error
 ↓
vulnerability uncertainty
 ↓
risk error/uncertainty
```

Assess whether an upstream error can materially change downstream conclusions.

## 12. Sensitivity audit

Verify sensitivity to material assumptions:

```text
reconstruction parameters
hazard model parameters
inventory assumptions
spatial resolution
temporal window
vulnerability weights
cutoffs
normalization
risk function
scenario assumptions
```

Record stable, conditionally stable and unstable conclusions where appropriate.

## 13. Double-counting audit

Search across the complete chain for:

```text
same source repeated
same variable repeated
exposure embedded in vulnerability and risk
hazard embedded in vulnerability without theory
correlated indicators hidden overweighting
same loss variable used as both calibration and validation
```

Material double-counting is a certification blocker until resolved or explicitly justified.

## 14. Coverage audit

Distinguish:

```text
covered
observed
modelled
estimated
gap
unknown
outside domain
```

Coverage gaps must not be displayed as confirmed absence.

## 15. Provenance completeness

Every research-ready artifact must have:

```text
source
source version/date
method
method version
parameters
processing history
spatial/temporal metadata
input references
output references
checksums where available
validation references
review status
```

## 16. Reproducibility audit

A certified pilot must permit a clean rerun from frozen inputs and declared environment.

Required evidence:

```text
run manifest
input versions
method versions
parameter set
environment/dependency record
random seed where applicable
output checksums
validation results
```

Reproducibility means the result can be regenerated under the declared environment; it does not mean every future software environment will reproduce it bit-for-bit.

## 17. Scientific finding severity

```text
CRITICAL
MAJOR
MODERATE
MINOR
OBSERVATION
```

CRITICAL findings affect validity, interpretation, provenance or safety of downstream use.

MAJOR findings require correction or explicit restriction before research-ready certification.

## 18. Certification states

```text
NOT_CERTIFIED
CONDITIONALLY_CERTIFIED
RESEARCH_READY
SUPERSEDED
REJECTED
```

`RESEARCH_READY` requires all critical gates to pass and all major limitations to be documented and acceptable for the declared use.

## 19. Certification decision matrix

```text
Critical failure present
→ NOT_CERTIFIED

No critical failure + unresolved major issue
→ CONDITIONALLY_CERTIFIED / restricted use

All critical gates pass + major limitations controlled
→ RESEARCH_READY

Older version replaced by certified successor
→ SUPERSEDED

Method/evidence fundamentally invalid for declared purpose
→ REJECTED
```

## 20. Pilot certification dossier

Generate a machine-readable and human-readable dossier containing:

```text
pilot_id
study question
geographic domain
temporal domain
event identity
evidence inventory
reconstruction version
hazard version
exposure version
vulnerability framework/version
risk model/version
validation summary
error register
uncertainty summary
sensitivity summary
coverage summary
provenance status
limitations
certification state
review date
reviewer/role
```

## 21. Research-ready gate

The pilot may enter `RESEARCH_READY` only when:

```text
identity resolved
critical evidence traceable
reconstruction validated for declared purpose
hazard semantics valid
exposure inventory traceable
vulnerability framework explicit
risk function explicit
cross-stage semantics consistent
material uncertainty disclosed
validation independence classified
material errors controlled
sensitivity assessed
provenance complete
reproducibility manifest complete
limitations documented
```

## 22. What certification does NOT mean

Certification does not mean:

```text
zero error
universal validity
causal proof
future prediction certainty
operational warning certification
policy authorization
complete representation of reality
```

## 23. Pilot release rule

Only certified products may be labelled:

```text
HG-SCRIS RESEARCH-READY
```

Exploratory products must retain their lower status in metadata and UI.

## 24. Versioning and supersession

If an upstream artifact changes materially:

```text
upstream version changes
        ↓
downstream dependency invalidated
        ↓
re-run affected stages
        ↓
re-validation
        ↓
re-certification
```

A stale downstream product must not remain marked research-ready.

## 25. Human scientific review

Automated QA cannot replace scientific judgement where interpretation, construct validity, causal assumptions or applicability require expertise.

The certification record must identify:

```text
automated checks
expert checks
unresolved judgement calls
```

## 26. Final 04-series gate tests

```text
identity/provenance test
semantic consistency test
CRS/spatial test
temporal consistency test
unit/scale test
coverage test
uncertainty lineage test
validation independence test
error propagation test
sensitivity test
double-counting test
reproducibility test
upstream-version invalidation test
handoff-state test
certification-state test
pilot dossier completeness test
```

## 27. Acceptance criteria

BUILD-04Z is accepted when:

- the entire 04-series has one auditable lineage chain;
- cross-stage semantic consistency is tested;
- spatial and temporal metadata are reconciled;
- units and scales are checked;
- uncertainty is audited end-to-end;
- validation independence is explicitly classified;
- material error propagation is assessed;
- sensitivity is audited;
- double-counting is checked across stages;
- coverage gaps are distinguishable from absence;
- provenance and reproducibility requirements are enforceable;
- upstream changes invalidate dependent certified outputs;
- human scientific review is explicitly separated from automated QA;
- certification states are enforceable;
- a pilot certification dossier can be generated;
- only qualifying pilots can receive the `HG-SCRIS RESEARCH-READY` designation.

## 28. 04-series completion gate

```text
04T REAL EVIDENCE
      ↓
04U VALIDATION
      ↓
04V HAZARD
      ↓
04W EXPOSURE
      ↓
04X VULNERABILITY
      ↓
04Y RISK
      ↓
04Z CROSS-STAGE CERTIFICATION
      ↓
HG-SCRIS v1.0 RESEARCH-READY GATE
```

## Next step

BUILD-05A — Scenario/Counterfactual Engine: reconstruct alternative event pathways and future states from the certified baseline while preserving causal assumptions, uncertainty, provenance and scenario comparability.
