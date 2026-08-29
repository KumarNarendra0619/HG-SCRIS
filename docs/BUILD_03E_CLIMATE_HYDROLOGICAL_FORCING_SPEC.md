# BUILD-03E — Climate, Rainfall, Snow & Hydrological Forcing Integration

## Objective
Create a reproducible forcing layer for event reconstruction and scenario modelling. Forcing data provide environmental inputs/context; they do not by themselves establish that an event occurred or define a hazard footprint.

## Core forcing groups

- precipitation: rainfall/snowfall where available
- temperature
- snow/ice indicators where available
- runoff
- discharge/streamflow where observed or modelled
- antecedent precipitation
- extreme precipitation indicators
- other event-specific meteorological/hydrological variables justified by the process model

## Source hierarchy

Prefer, in order:

1. observed gauge / official hydrological records where accessible
2. authoritative gridded/reanalysis products
3. validated satellite precipitation/snow products
4. peer-reviewed event datasets/models
5. secondary sources for supporting evidence

A gridded/reanalysis product must not be described as a local gauge observation.

## Event-window design

For each event, define explicitly:

- baseline period
- antecedent period
- trigger window
- response window
- post-event period

The exact windows are event- and process-specific. No universal rainfall threshold is hard-coded.

## Temporal QA

Check:

- coverage contains event date/time
- time zone / timestamp convention
- time step
- missing intervals
- duplicate timestamps
- temporal aggregation method
- event-window completeness

## Spatial QA

Check:

- grid/raster geometry
- CRS
- resolution
- basin/valley representation
- orographic limitations
- gauge representativeness
- resampling method

## Forcing normalization

Store native values and units as received. Any converted/aggregated product must record:

`source → conversion → aggregation → output`

Do not overwrite the native dataset.

## Rainfall handling

Rainfall products may be used to identify spatial/temporal precipitation patterns and event forcing. Valley-scale conclusions require appropriate validation. Where gauges exist, calibration/validation can be added as a separate documented step.

## Snow / temperature

Use only variables justified by the event mechanism. For example, rainfall-triggered flooding, GLOF, avalanche, landslide and compound events can require different forcing sets.

## Hydrological discharge

Observed discharge is preferred where available. Modelled runoff/discharge must be labelled as modelled and must retain model/source metadata. Discharge is not interchangeable with precipitation.

## Antecedent forcing

For event reconstruction, calculate documented antecedent metrics such as cumulative precipitation over defined windows only when scientifically justified. Windows must be stored in configuration rather than hidden in code.

## Event attribution safeguard

Correlation is not causal attribution. High rainfall around an event does not prove rainfall caused the event. Trigger attribution must be supported by event evidence and process analysis.

## Missing-data policy

Missing values are not automatically zero. The system must distinguish:

- observed zero
- missing
- not available
- outside coverage
- quality flagged

## Uncertainty

Forcing uncertainty should be carried into later scenario/validation stages where possible. Do not create false precision by reporting more significant digits than supported by the source.

## Outputs

`forcing_master`

`precipitation_event_window`

`temperature_event_window`

`snow_ice_event_context`

`hydrological_event_context`

`forcing_qa`

`forcing_manifest`

## Integration with HG-SCRIS

`forcing + DEM + hydrography + cryosphere + event evidence → reconstruction/scenario engine`

Forcing data are inputs to the model, not the final risk result.

## Reproducibility

Every forcing extraction must record dataset version, source, spatial subset, temporal subset, unit conversion, aggregation, calibration (if any), configuration and lineage.

## Acceptance gate

BUILD-03E is complete for a pilot only when the required forcing datasets are source-registered, temporally and spatially QA'd, normalized without loss of native provenance, and available to the event-reconstruction pipeline with reproducible manifests.

## Next step
BUILD-03F — Historical Event Evidence & Event Reconstruction Data Integration.
