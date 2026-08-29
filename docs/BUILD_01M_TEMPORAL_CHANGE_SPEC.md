# BUILD-01M — Temporal Glacier–Lake Change Engine

## Objective
Turn static glacier/lake inventories into dated, reproducible time series that can feed trigger screening, event reconstruction and future scenarios.

## Core model

`Observation = entity + date + variable + value + source + uncertainty`

Temporal analysis must retain the acquisition/observation date and source for every value. Different years or products must not be silently merged.

## Supported change metrics

- absolute change
- relative change
- annualized absolute change
- multi-observation time series

Potential variables include glacier area, terminus position, lake area, elevation, volume/depth estimates, velocity and other sourced indicators.

## Quality controls

1. Parse and validate dates.
2. Require stable entity IDs.
3. Require source metadata.
4. Sort observations chronologically.
5. Do not silently impute missing values.
6. Treat zero baselines as undefined for relative change.
7. Preserve source changes between first and last observations.
8. Retain uncertainty when available.

## Remote-sensing integration boundary
Satellite/DEM products can be ingested by a later data-adapter layer. This build intentionally contains no hidden claims about a specific satellite product, revisit interval or classification accuracy. Those choices must be documented per variable and study period.

## Trigger integration
Temporal change is an input to trigger screening, not proof of imminent failure. A lake expanding rapidly may warrant prioritisation, but failure probability requires process-based evidence and calibration.

## Event reconstruction
For historical events, pre-event and post-event observations will be kept separate from reconstructed/modelled values. The temporal engine supports before/after comparisons and event-window extraction.

## Future scenario pathway

`Historical observations → trend/change characterization → scenario assumptions → future hazard simulation`

Trend extrapolation must not be presented as a physical forecast unless the underlying process model supports it.

## Planned outputs

- entity-level time series
- first/last change table
- annualized change metrics
- change direction/status
- uncertainty/provenance metadata
- event-window comparisons
- trigger-screening inputs
