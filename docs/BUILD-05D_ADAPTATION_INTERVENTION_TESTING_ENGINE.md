# BUILD-05D — Adaptation / Intervention Testing Engine

## Status
ADAPTATION / INTERVENTION TESTING CONTRACT LOCKED

## Purpose
BUILD-05D tests explicit adaptation and intervention options against the certified baseline and registered scenario/pathway states. It estimates potential changes in hazard, exposure, vulnerability and risk, while keeping intervention assumptions, implementation constraints, uncertainty, trade-offs and residual risk explicit.

This engine does **not** treat a modelled intervention effect as a guaranteed causal impact.

## 1. Core scientific chain

```text
CERTIFIED BASELINE
      ↓
SCENARIO / FUTURE PATHWAY
      ↓
INTERVENTION DEFINITION
      ↓
IMPLEMENTATION ASSUMPTIONS
      ↓
SYSTEM RESPONSE MODEL
      ↓
RISK / OUTCOME RESPONSE
      ↓
RESIDUAL RISK
      ↓
UNCERTAINTY + SENSITIVITY
      ↓
TRADE-OFF / EQUITY AUDIT
      ↓
ROBUSTNESS
```

## 2. Intervention contract

Every intervention declares:

```text
intervention_id
intervention_version
baseline_ref
scenario/pathway_ref
target system/place/population/asset
intervention class
start time
duration
coverage
intensity/scale
implementation assumptions
effect mechanism
expected response variables
cost/resource fields where available
uncertainty
constraints
limitations
```

## 3. Adaptation vs mitigation vs intervention

Metadata distinguishes:

```text
ADAPTATION
= adjustment intended to reduce harm/vulnerability or improve resilience

MITIGATION
= action intended to reduce the driver/source of a hazard where applicable

INTERVENTION
= broader controlled action applied to a target system
```

The system must not infer the classification from the intervention name alone.

## 4. Intervention classes

Support registered classes such as:

```text
structural
nature-based
infrastructure
land-use/planning
early-warning / preparedness
service-access
relocation / managed retreat
social protection
health/public-health
livelihood diversification
water management
waste management
ecosystem restoration
policy/regulatory
hybrid / portfolio
```

## 5. Effect mechanism registry

Every intervention effect should specify:

```text
intervention
      ↓
mechanism
      ↓
intermediate variable
      ↓
H/E/V change
      ↓
risk/outcome change
```

If the mechanism is assumption-based, it must be labelled as such.

## 6. Effectiveness model

Intervention effectiveness may be:

```text
deterministic
bounded
probabilistic
empirically estimated
scenario-conditioned
expert-elicited with documented protocol
```

A default effectiveness of 100% is prohibited.

## 7. Coverage and implementation realism

Modelled effectiveness must be separated from implementation coverage:

```text
technical effectiveness
        ×
actual coverage
        ×
implementation fidelity
        ↓
realized effect assumption
```

These terms must not be silently collapsed.

## 8. Timing and adaptation dynamics

Support:

```text
immediate response
short-term intervention
seasonal adaptation
annual implementation
phased adaptation
long-term adaptation
adaptive management
```

Delayed effects and implementation lag must be explicit.

## 9. Baseline / intervention comparison

Minimum comparison:

```text
No-intervention outcome
        −
Intervention outcome
        =
Potential avoided impact
```

This is a modelled scenario contrast unless an appropriate causal design and observed implementation evidence support a causal effect claim.

## 10. Residual risk

The engine explicitly retains:

```text
baseline risk
      ↓
intervention
      ↓
residual risk
```

Residual risk cannot be silently set to zero.

## 11. Risk transfer audit

Check whether an intervention:

```text
reduces risk in one place
but increases risk elsewhere
```

or:

```text
reduces one hazard
but increases another
```

Potential transfers include spatial, temporal, sectoral, population and hazard-to-hazard transfer.

## 12. Cascading and compound effects

Intervention effects may propagate through:

```text
Intervention
   ↓
Primary system response
   ↓
Secondary system response
   ↓
Cascading impact
   ↓
Net risk response
```

Each material link requires explicit modelling or assumption metadata.

## 13. Equity and distributional audit

Do not assess only mean risk reduction.

Where data permit, examine:

```text
who benefits?
who bears residual risk?
who is excluded?
which locations gain/lose?
which population groups gain/lose?
distribution of avoided impact
```

Equity analysis is descriptive unless a formal inferential/causal design is specified.

## 14. Cost and resource module

Where reliable data exist, interventions may include:

```text
capital cost
operating cost
maintenance cost
implementation resource
coverage cost
lifetime cost
```

Cost fields are optional and must not be fabricated.

## 15. Cost-effectiveness / efficiency

Where valid:

```text
cost per avoided unit of impact
cost per person protected
cost per unit risk reduction
benefit-cost ratio
```

The denominator, valuation basis, discounting assumptions and time horizon must be explicit where applicable.

Economic metrics must not be compared across interventions without compatible valuation assumptions.

## 16. Portfolio interventions

Multiple interventions can be evaluated as:

```text
A
B
C
A+B
A+C
A+B+C
```

The engine must test whether combined effects are:

```text
additive
sub-additive
super-additive
unknown
```

unless the interaction mechanism is explicitly modelled.

## 17. Interaction safeguards

Do not assume:

```text
Effect(A+B) = Effect(A) + Effect(B)
```

unless justified by the model/evidence.

Potential interactions and double-counting must be audited.

## 18. Uncertainty architecture

Separate:

```text
baseline uncertainty
scenario uncertainty
intervention-effect uncertainty
coverage uncertainty
implementation uncertainty
model uncertainty
parameter uncertainty
cost uncertainty
behavioral/adoption uncertainty
```

Do not reduce these to one unexplained confidence score.

## 19. Sensitivity analysis

Test material assumptions:

```text
intervention effectiveness
coverage
adoption
implementation fidelity
timing
maintenance
cost
hazard intensity
exposure trajectory
vulnerability response
interaction assumptions
```

Classify conclusions as robust or assumption-sensitive.

## 20. Robustness classes

```text
ROBUST
CONDITIONALLY ROBUST
EFFECTIVENESS-SENSITIVE
IMPLEMENTATION-SENSITIVE
COST-SENSITIVE
MODEL-SENSITIVE
DATA-LIMITED
CONFLICTING
UNRESOLVED
```

## 21. Adaptation limits

The engine records when intervention effectiveness is bounded by:

```text
physical limits
institutional capacity
financial constraints
spatial constraints
maintenance requirements
social acceptance
behavioral response
compound hazard conditions
```

These constraints must be visible in the output.

## 22. Maladaptation audit

Flag interventions that may:

```text
increase long-term vulnerability
transfer risk
create lock-in
increase exposure elsewhere
reduce adaptive capacity
produce unequal protection
create new cascading hazards
```

A reduction in one modelled risk metric does not automatically mean an intervention is adaptive in the broader system.

## 23. No-intervention comparator

Every intervention test must define an appropriate comparator:

```text
current baseline
business-as-usual
no-intervention pathway
alternative intervention
```

The comparator must be versioned.

## 24. Intervention scenario matrix

Generate:

```text
Intervention
Coverage
Effectiveness
Cost
Residual risk
Avoided impact
Uncertainty
Sensitivity
Equity flag
Maladaptation flag
Robustness
```

## 25. Validation strategy

Where intervention outcomes are observed:

```text
observed implementation
      ↓
observed outcome
      ↓
independent evaluation
```

Where future intervention outcomes are unavailable:

```text
mechanism validation
historical evidence
quasi-experimental evidence where appropriate
expert evidence with protocol
sensitivity analysis
scenario plausibility
```

Future modelled effects must not be labelled observed causal effects.

## 26. Causal effect safeguard

A modelled intervention contrast is reported as:

```text
potential avoided impact
scenario-conditioned effect
modelled risk reduction
```

unless a suitable causal identification design supports stronger language.

## 27. Implementation uncertainty

Separate:

```text
can it work?
        ↓
will it be implemented?
        ↓
will it reach the target?
        ↓
will it be maintained?
        ↓
what residual effect remains?
```

Technical efficacy must not be confused with realized effectiveness.

## 28. Spatial intervention testing

Support:

```text
site-specific intervention
zonal intervention
corridor/network intervention
watershed intervention
settlement-level intervention
population-targeted intervention
```

Spatial allocation assumptions must be explicit.

## 29. Temporal intervention testing

Support:

```text
before-event
between events
seasonal
phased
continuous
adaptive trigger-based
```

Trigger rules must be versioned and scientifically justified.

## 30. Adaptive management

Where sequential decisions are tested:

```text
State observation
      ↓
Decision rule
      ↓
Intervention
      ↓
New state
      ↓
Reassessment
      ↓
Next decision
```

This is a dynamic policy pathway, not a guarantee of optimal adaptation.

## 31. Quality states

```text
DRAFT
QA_FAILED
EXPLORATORY
SIMULATION_READY
VALIDATION_PENDING
VALIDATED_WITH_LIMITATIONS
RESEARCH_READY
SUPERSEDED
REJECTED
```

## 32. Output contract

```text
intervention_run_id
intervention_version
baseline_ref
scenario_ref
pathway_ref
intervention_ref
comparator_ref
target_ref
effect_model_ref
coverage_ref
implementation_ref
outcome_artifacts[]
avoided_impact_ref
residual_risk_ref
cost_ref where available
uncertainty_ref
sensitivity_ref
equity_ref
maladaptation_ref
validation_ref
robustness_class
limitations
quality_state
```

## 33. Invalidation

If the baseline, scenario, risk model, intervention model or material evidence changes:

```text
dependency changes
      ↓
intervention result = STALE
      ↓
re-execution
      ↓
re-validation where applicable
      ↓
new version
```

## 34. Stop conditions

Block or downgrade when:

```text
baseline not certified
comparator undefined
intervention mechanism undefined
100% effectiveness silently assumed
coverage ignored
implementation constraints ignored
units incompatible
causal effect claimed without identification design
cost data fabricated
combined intervention effects double-counted
material residual risk hidden
risk transfer ignored
critical uncertainty omitted
model outside applicability domain
```

## 35. First validated intervention product

Keep the first pilot narrow:

```text
ONE certified baseline
      ↓
ONE registered future/scenario pathway
      ↓
ONE intervention
      ↓
ONE comparator
      ↓
ONE primary outcome
      ↓
RESIDUAL RISK
      ↓
UNCERTAINTY + SENSITIVITY
      ↓
EQUITY + MALADAPTATION AUDIT
      ↓
ROBUSTNESS
```

## 36. Acceptance tests

```text
intervention schema test
baseline/comparator test
effect-mechanism test
effectiveness-bound test
coverage test
implementation-fidelity test
timing test
residual-risk test
risk-transfer test
cascade test
equity test
cost-data integrity test
portfolio interaction test
uncertainty test
sensitivity test
maladaptation test
causal-claim test
spatial allocation test
temporal trigger test
provenance test
invalidation test
reproducibility test
```

## 37. Acceptance criteria

BUILD-05D is accepted when:

- interventions are explicit, versioned and linked to certified baselines/scenarios;
- mechanisms and effectiveness assumptions are declared;
- technical efficacy is separated from coverage and implementation fidelity;
- residual risk is retained;
- risk transfer and cascading effects are audited;
- distributional/equity effects are visible where data permit;
- costs are used only when supported by reliable data;
- combined intervention effects are not assumed additive without justification;
- uncertainty and sensitivity are explicit;
- maladaptation risks are screened;
- causal effect claims are gated by appropriate identification evidence;
- future intervention effects are not labelled observed outcomes;
- dependencies invalidate stale outputs;
- a bounded intervention product can be reproduced under the declared environment.

## 38. Transition

```text
05A SCENARIO / COUNTERFACTUAL
        ↓
05B FUTURE STATE / PATHWAY
        ↓
05C COMPARISON + ROBUSTNESS
        ↓
05D ADAPTATION / INTERVENTION TESTING
        ↓
05E DECISION / POLICY STRESS TEST
```

## Next step

BUILD-05E — Decision / Policy Stress-Test Engine: evaluate intervention portfolios and scenario pathways under multiple objectives, constraints, shocks and uncertainty to identify robust, fragile and no-regret decision options without converting model outputs into automatic policy prescriptions.
