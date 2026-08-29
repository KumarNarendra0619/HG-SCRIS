# HG-SCRIS Scientific Specification

## Project
Himalayan Glacier-to-Settlement Cascade Risk Intelligence System (HG-SCRIS)

Version: 0.1.0
Stage: BUILD-01A

## Purpose
HG-SCRIS is a research-grade geospatial decision-support and scenario-modelling platform for identifying, reconstructing and visualizing plausible glacier-origin hazard cascades and downstream exposure, risk, impact, evacuation and safety conditions.

## Core chain
Glacier → Trigger → Cascade → Tributary/River → Settlement → Impact → Risk → Evacuation → Safety

## Scientific modes
1. Event Reconstruction: reconstruct documented historical events from observed evidence and compare observed and modelled pathways.
2. Future Scenario: evaluate defined plausible scenarios. Scenario outputs are not deterministic forecasts.

## Core spatial unit
The Glacier-to-Settlement (G2S) unit links a glacier/source zone with its outlet, hydrological network, downstream settlements and relevant infrastructure.

## Hazard classes
- GLOF
- Ice/glacier collapse
- Rock–ice avalanche
- Landslide-dammed lake
- Debris flow
- Extreme rainfall–glacier compound event
- Flash flood/river flood
- Compound cascade

## Core analytical modules
Glacier, terrain, hydrology, lakes, hazards, cascade, exposure, risk, evacuation, reconstruction, simulation, validation and visualization.

## Risk concept
Risk is evaluated conceptually as Hazard × Exposure × Vulnerability. Risk and observed/modelled impact remain separate outputs.

## Uncertainty
All major derived outputs must carry confidence and/or uncertainty information. Observed, reconstructed, modelled and scenario information must remain explicitly distinguishable.

## Reproducibility
Each result must be traceable to dataset version, method ID, parameters, code version and processing date.

## Claim boundary
HG-SCRIS identifies, reconstructs and visualizes plausible glacier-origin cascading hazard pathways and evaluates downstream exposure, risk, impact and evacuation/safety conditions under defined scenarios. It is not an all-Himalaya deterministic early-warning or exact future-event prediction system.
