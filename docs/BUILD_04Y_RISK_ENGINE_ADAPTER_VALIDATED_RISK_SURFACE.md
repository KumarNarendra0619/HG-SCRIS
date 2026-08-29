# BUILD-04Y — Risk Engine Adapter, Hazard–Exposure–Vulnerability Integration & First Validated Risk Surface

## Status
RISK ENGINE CONTRACT LOCKED

## Purpose
Integrate validated hazard, exposure and vulnerability products into an explicit, versioned and reproducible risk model. BUILD-04Y prevents the common methodological error of treating a hazard map, exposure count, or vulnerability index as risk by itself. Risk is produced only through a declared analytical function whose variables, units, assumptions, uncertainty treatment and applicability are explicit.

## 1. Core scientific chain

```text
VALIDATED HAZARD
       +
VALIDATED EXPOSURE
       +
VALIDATED VULNERABILITY
       ↓
RISK FUNCTION / MODEL
       ↓
RISK ESTIMATION
       ↓
UNCERTAINTY PROPAGATION
       ↓
VALIDATION / SENSITIVITY
       ↓
VALIDATED RISK SURFACE
       ↓
DECISION / SCENARIO HANDOFF
```

The engine must not silently multiply incompatible indices.

## 2. Risk definition contract

Every risk model declares:

```text
risk_model_id
risk_model_version
theoretical basis
risk definition
hazard input
exposure input
vulnerability input
outcome/loss variable
spatial support
temporal support
functional form
parameters
weights where applicable
uncertainty method
validation strategy
applicability domain
limitations
```

A product labelled simply `risk` without these semantics is not research-ready.

## 3. Risk model families

Support registered model classes such as:

```text
qualitative risk matrix
index-based risk
multiplicative formulation
probabilistic risk
expected-loss model
damage-function model
scenario-based risk
multi-hazard risk
network/system risk
spatial statistical risk
other scientifically registered formulations
```

The platform must not assume that one equation is universally correct.

## 4. Canonical conceptual distinction

```text
HAZARD
= potentially damaging physical/environmental process or condition

EXPOSURE
= people/assets present in the hazard-relevant space/time

VULNERABILITY
= susceptibility/capacity characteristics determining propensity to harm

RISK
= modelled potential for adverse consequences under a declared framework
```

Exact definitions remain framework-dependent and must be registered.

## 5. Input compatibility gate

Before risk calculation:

```text
hazard semantics compatible?
exposure unit compatible?
vulnerability meaning compatible?
spatial support aligned?
temporal support aligned?
reference period aligned?
coverage adequate?
uncertainty available?
```

Failure blocks or downgrades the risk run.

## 6. Spatial integration

Support:

```text
cell-wise integration
polygon-zone integration
asset-level risk
network-segment risk
settlement-level risk
administrative aggregation
watershed/catchment aggregation
custom analytical units
```

Spatial aggregation must preserve source support and prevent false precision.

## 7. Temporal integration

Risk may be represented as:

```text
event-specific
seasonal
annual
multi-year
scenario-specific
time-dependent
```

The model must declare how hazard timing, exposure timing and vulnerability reference period are reconciled.

## 8. Risk function registry

Example registered functions may include:

```text
R = f(H, E, V)

R = H × E × V

R = P(H) × E × V

Expected Loss = P(event) × Exposure × Vulnerability/Damage Function
```

These are examples, not universal prescriptions. Units and interpretation must be checked before execution.

## 9. Index compatibility safeguard

If H, E and V are normalized indices, the engine must record:

```text
scale
range
normalization
meaning of zero
meaning of one
weighting
aggregation
```

Multiplying three arbitrary normalized scores does not automatically produce a physically meaningful risk quantity.

## 10. Physical-loss pathway

Where quantitative loss estimation is justified:

```text
Hazard intensity
      ↓
Damage / fragility function
      ↓
Asset-specific damage ratio
      ↓
Exposed asset value
      ↓
Expected / scenario loss
```

A generic vulnerability score must not be silently interpreted as a damage ratio.

## 11. Probabilistic risk

Where event probabilities are available:

```text
hazard probability distribution
        ↓
exposure distribution
        ↓
vulnerability/damage relationship
        ↓
loss/risk distribution
```

Store central estimate and distribution/interval information where supported.

## 12. Multi-hazard risk

Multi-hazard integration must distinguish:

```text
independent hazards
co-occurring hazards
sequential hazards
cascading hazards
compound hazards
interacting hazards
```

Aggregation rules and interaction mechanisms must be registered. Simple addition of hazard scores does not establish compound physical risk.

## 13. Cascading risk

Where one hazard changes another component:

```text
Hazard A
   ↓
System state change
   ↓
Hazard B / exposure change / vulnerability change
   ↓
Cascading consequence
```

The causal pathway must be represented explicitly rather than inferred from spatial overlap alone.

## 14. Risk uncertainty

Track:

```text
hazard uncertainty
exposure uncertainty
vulnerability uncertainty
parameter uncertainty
model/structural uncertainty
scenario uncertainty
spatial uncertainty
temporal uncertainty
```

If formal probabilistic propagation is not defensible, use declared bounded, qualitative or sensitivity-based treatment.

## 15. Sensitivity analysis

Test material influence of:

```text
risk function
hazard weighting
exposure definition
vulnerability weights
cutoffs
normalization
parameters
spatial scale
temporal window
missing-data treatment
scenario assumptions
```

Report rank/score stability where appropriate.

## 16. Validation framework

Risk validation is outcome-dependent. Possible evidence includes:

```text
observed event losses
damage assessments
insurance/compensation records where legally and ethically usable
field surveys
independent post-event inventories
historical loss databases
expert validation
out-of-sample event validation
```

Validation data must be independent of model calibration data where independence is claimed.

## 17. Error analysis

Assess:

```text
bias
MAE/RMSE where appropriate
classification performance
spatial displacement
under/over-estimation
false hotspot / missed hotspot
scenario error
calibration error
```

A risk map is not validated merely because its hotspots appear plausible.

## 18. Calibration policy

```text
CALIBRATION DATA
      ↓
PARAMETER ESTIMATION
      ↓
NEW MODEL VERSION
      ↓
INDEPENDENT VALIDATION
```

No calibration evidence may be relabelled as independent validation.

## 19. Risk quality states

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

## 20. First validated risk surface

The first pilot must remain bounded:

```text
ONE validated hazard
       +
ONE validated exposure
       +
ONE validated vulnerability
       ↓
ONE registered risk function
       ↓
ONE spatial/temporal domain
       ↓
VALIDATION + SENSITIVITY
       ↓
FIRST VALIDATED RISK SURFACE
```

Do not construct a multi-hazard national risk index before the single-event analytical chain has passed validation.

## 21. Risk output contract

```text
risk_id
risk_model_id
risk_model_version
hazard_ref
exposure_ref
vulnerability_ref
risk_variable
unit
spatial_support
temporal_support
score_definition
artifact_ref
uncertainty_ref
validation_refs[]
sensitivity_ref
limitations
quality_state
handoff_status
```

## 22. Decision/scenario handoff

Risk output may support:

```text
scenario comparison
priority screening
spatial planning
resource allocation analysis
adaptation assessment
preparedness planning
research interpretation
```

Operational decisions require a separate governance/decision-use declaration and must not be implied solely by a `RESEARCH_READY` state.

## 23. Decision-use safeguards

```text
research result
≠
operational warning
≠
policy mandate
```

The platform must expose uncertainty, limitations, validation state and data date whenever risk results are presented for decision support.

## 24. Equity and ethical safeguards

Risk ranking must not be interpreted as ranking the value of communities or persons.

Where demographic vulnerability is used:

```text
aggregation level disclosed
sensitive attributes protected
stigma-producing labels avoided
uncertainty disclosed
historical/systemic data limitations documented
```

## 25. Reproducibility manifest

Record:

```text
risk run ID
hazard version
exposure version
vulnerability version
risk-model version
parameters
weights
normalization
spatial/temporal parameters
scenario definition
code/environment
input checksums
output checksums
validation results
sensitivity results
uncertainty
review state
```

## 26. Stop conditions

Block or downgrade when:

```text
hazard/exposure/vulnerability semantics incompatible
risk function undefined
units incompatible
spatial alignment unresolved
temporal alignment unresolved
critical input uncertainty missing
calibration/validation leakage
unsupported loss interpretation
provenance incomplete
model outside applicability domain
```

## 27. Acceptance tests

```text
input compatibility test
risk-definition test
unit compatibility test
spatial alignment test
temporal alignment test
risk-function registration test
index compatibility test
physical-loss semantic test
probabilistic propagation test
multi-hazard interaction test
cascading-risk test
calibration leakage test
validation test
sensitivity test
uncertainty test
provenance test
quality-state test
handoff test
blocked-risk test
reproducibility test
```

## 28. Acceptance criteria

BUILD-04Y is accepted when:

- hazard, exposure and vulnerability remain distinct inputs;
- every risk run uses a registered risk function/model;
- units and semantic compatibility are checked;
- spatial and temporal supports are explicit;
- normalized indices cannot be blindly interpreted as physical loss;
- physical damage pathways are explicitly modelled where used;
- multi-hazard and cascading mechanisms require registered rules;
- uncertainty from upstream layers is retained;
- calibration is separated from independent validation;
- risk validation uses appropriate outcome/reference evidence;
- sensitivity analysis is operational;
- quality and handoff states are explicit;
- decision-use limitations are disclosed;
- critical failures block silent downstream use;
- the first bounded validated risk surface can be produced reproducibly.

## Next step

BUILD-04Z — Cross-Stage Scientific QA, End-to-End Provenance Audit, Uncertainty Propagation Audit, Pilot Certification & HG-SCRIS v1.0 Research-Ready Gate.
