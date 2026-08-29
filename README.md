# HG-SCRIS

**Himalayan Glacier-to-Settlement Cascade Risk Intelligence System**

A research-grade geospatial decision-support and scenario-modelling platform for identifying, reconstructing and visualizing plausible glacier-origin hazard cascades and downstream exposure, risk, impact, evacuation and safety conditions.

## Core analytical chain

**Glacier → Trigger → Cascade → Tributary/River → Settlement → Impact → Risk → Evacuation → Safety**

## Development status

**BUILD-01A — Repository Initialization — v0.1.0**

The repository is being built as a reproducible research system. Data provenance, method identifiers, validation and uncertainty are mandatory components.

## Scientific modes

- **Event Reconstruction:** reconstruct documented historical events from observed evidence and compare observed and modelled pathways.
- **Future Scenario:** evaluate defined plausible scenarios. Scenario outputs are not deterministic forecasts.

## Repository map

- `docs/` — scientific specification, data and methods
- `config/` — reproducible project/model configuration
- `notebooks/` — Google Colab research workflows
- `src/hgscris/` — production Python modules
- `tests/` — automated tests
- `data/` — raw/interim/processed/derived/validation lifecycle
- `outputs/` — maps, tables, models and animations
- `app/` — future web application

## Scientific claim boundary

HG-SCRIS identifies, reconstructs and visualizes plausible glacier-origin cascading hazard pathways and evaluates downstream exposure, risk, impact and evacuation/safety conditions under defined scenarios. It is not an all-Himalaya deterministic early-warning or exact future-event prediction system.

## Reproducibility rule

Every production result must be traceable to dataset version, method ID, parameters, code version, processing date and confidence/uncertainty information.
