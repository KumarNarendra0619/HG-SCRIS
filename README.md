# HG-SCRIS

**Himalayan Glacier-to-Settlement Cascade Risk Intelligence System**

A research-grade geospatial decision-support and scenario-modelling platform for identifying, reconstructing and visualizing plausible glacier-origin hazard cascades and downstream exposure, risk, impact, evacuation and safety conditions.

## Core analytical chain

**Glacier → Trigger → Cascade → Tributary/River → Settlement → Impact → Risk → Evacuation → Safety**

## Development status

**AUDIT-02 — Configuration, Schema & Cross-Stage Contract Consistency — v0.6.1**

The architecture through BUILD-06E is frozen for audit. The repository is now aligning executable configuration and cross-stage contracts before synthetic end-to-end testing. This is not yet a research-ready or v1.0 release.

## Scientific modes

- **Event Reconstruction:** reconstruct documented historical events from observed evidence and compare observed and modelled pathways.
- **Future Scenario:** evaluate defined plausible scenarios. Scenario outputs are not deterministic forecasts.

## Scientific evidence states

Production outputs must preserve the distinction between **OBSERVED, INFERRED, MODELLED, SCENARIO, and UNCERTAIN** states.

## Confidence states

Claim-specific confidence uses the declared qualitative states **HIGH SUPPORT, MODERATE SUPPORT, LIMITED SUPPORT, LOW SUPPORT, and UNRESOLVED**. Confidence is not a probability of event occurrence.

## Repository map

- `docs/` — scientific specification, data and methods
- `config/` — reproducible project/model configuration
- `notebooks/` — Google Colab research workflows
- `src/hgscris/` — production Python modules
- `tests/` — automated tests
- `data/` — raw/interim/processed/derived/validation lifecycle
- `outputs/` — maps, tables, models and animations
- `app/` — future web application

## Spatial reference rule

EPSG:4326 is the storage/exchange CRS. Distance, area, slope, routing and other metric operations must use an explicitly declared project-local projected analysis CRS. The system must not silently treat geographic coordinates as metric coordinates.

## Scientific claim boundary

HG-SCRIS identifies, reconstructs and visualizes plausible glacier-origin cascading hazard pathways and evaluates downstream exposure, risk, impact and evacuation/safety conditions under defined scenarios. It is not an all-Himalaya deterministic early-warning or exact future-event prediction system.

## Reproducibility rule

Every production result must be traceable to dataset version, method ID, parameters, code version, processing date, scientific state, confidence and relevant uncertainty/source references.
