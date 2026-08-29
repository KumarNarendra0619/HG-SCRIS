# BUILD-01T — Risk & Impact Engine

## Objective
Combine scenario-specific hazard intensity, exposure, vulnerability and probability/weighting into transparent risk and impact outputs.

## Scientific decomposition

`Hazard × Exposure × Vulnerability × Probability/Scenario Weight → Risk/Expected Impact`

The exact mathematical model is process- and dataset-dependent. The repository therefore separates the components rather than embedding a universal Himalayan risk equation.

## Inputs

### Hazard
- process type
- intensity metrics such as depth, velocity, pressure or deposited thickness where physically modelled
- spatial extent
- arrival time
- scenario/model version
- uncertainty

### Exposure
- population
- buildings
- roads/bridges
- schools
- health/emergency facilities
- utilities and critical infrastructure
- economic/environmental assets where defined

### Vulnerability
Vulnerability functions must be explicitly sourced, calibrated or justified. Values are not inferred merely from elevation, distance or population.

### Probability / scenario weighting
Where a defensible event probability is unavailable, results remain scenario-specific rather than being presented as annualized probability-based risk.

## Current deterministic primitives

`expected_loss()` computes a transparent scenario-weighted loss from explicitly supplied normalized hazard intensity, exposure value, vulnerability and probability.

`risk_class()` provides a generic normalized screening classification with configurable thresholds. Default thresholds are placeholders for software testing and must not be presented as calibrated Himalayan risk thresholds.

## Impact dimensions
Separate outputs should be retained for:

- population impact
- building impact
- transport disruption
- critical-facility impact
- economic impact
- environmental impact
- accessibility/connectivity disruption

Avoid collapsing these into a single index unless the research design explicitly justifies the aggregation.

## Scenario matrix
For each source and process, support:

- low/reference scenario
- moderate scenario
- high scenario
- extreme/plausible upper scenario

The actual parameter ranges must come from event evidence, literature, physical modelling and/or calibration—not arbitrary percentages.

## Uncertainty
Risk outputs must preserve uncertainty from:

- source volume/discharge
- DEM resolution
- routing assumptions
- hazard-model parameters
- exposure data completeness
- vulnerability functions

Sensitivity/ensemble analysis should be used where parameter uncertainty is material.

## Historical event reconstruction
Observed impact and modelled impact are separate layers. Model performance is assessed using observed evidence; observations are never altered to improve model fit.

## Safety classification
For public-facing outputs, distinguish:

- modelled hazard
- potential exposure
- scenario risk
- observed historical impact
- validated evacuation/safety information

The platform must not present a research model as an official warning or evacuation order.

## Outputs

- hazard-intensity layer
- exposure-impact table
- scenario risk layer
- expected-loss metrics where justified
- uncertainty layer/range
- sensitivity diagnostics
- source/event comparison
- model validation report

## Next integration
BUILD-01U will transform validated scenario footprints and travel-time outputs into evacuation and safety analysis, including safe-zone suitability and route accessibility constraints.
