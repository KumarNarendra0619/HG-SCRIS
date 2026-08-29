# BUILD-04 — Real Data-to-Working-System Implementation Plan

## Status
LOCKED implementation gate. BUILD-04 starts the executable phase of HG-SCRIS. Previous BUILD-03 specifications remain the scientific contract; implementation must conform to them.

## Objective
Convert the HG-SCRIS architecture into a reproducible working pilot using real data, beginning with a controlled Himalayan pilot and then scaling toward All-Himalaya coverage.

## Non-negotiable principle
Do not attempt All-Himalaya high-resolution modelling first. Build one complete, auditable vertical slice from real source data to web visualization, validate it, then scale.

## Target vertical slice

`real glacier → real lake/source → DEM → hydrography → downstream trace → real settlement/exposure → documented event → reconstructed hazard → impact/risk → evacuation candidate analysis → 2D map → 3D scene → time animation → reproducibility manifest`

## Phase 04-0 — Repository readiness

Audit and standardize:

- repository structure
- Python environment
- dependency pinning
- configuration
- schemas
- notebooks
- source modules
- tests
- data directories
- output directories
- GitHub Actions
- documentation index

No large source datasets should be committed directly when repository-hosting limits make that inappropriate. Store source metadata and reproducible download/access manifests instead.

## Phase 04-1 — Source Data Registry

Create machine-readable registry for each dataset:

- dataset_id
- provider
- title
- URL/access mechanism
- license/terms
- spatial coverage
- temporal coverage
- resolution/scale
- CRS
- format
- variables
- update date
- access date
- quality notes
- intended use
- citation

Every downstream dataset must carry dataset_id and lineage.

## Phase 04-2 — Pilot AOI

Select one documented Himalayan event/AOI that contains, as far as practical:

- glacier/lake source
- terrain
- connected drainage
- settlements
- infrastructure
- event evidence
- enough data for independent checking

Pilot selection must be justified scientifically, not merely because it is visually interesting.

## Phase 04-3 — Automated ingestion

Build Python/Colab ingestion functions for:

- glacier inventory
- glacial lakes
- DEM
- river/tributary network
- settlements/population
- infrastructure
- event evidence
- imagery/event footprints where legally and technically accessible

All ingestion produces raw immutable snapshots plus metadata manifests.

## Phase 04-4 — Automated spatial QA

Checks include:

- CRS
- geometry validity
- duplicate IDs
- missing identifiers
- invalid/null geometries
- attribute domains
- spatial overlap anomalies
- topology
- elevation/range plausibility
- network connectivity
- temporal metadata
- source completeness

QA results are machine-readable and human-readable.

## Phase 04-5 — Standardized analytical data model

Convert sources to HG-SCRIS canonical schemas while retaining original IDs and fields.

Core entities:

`glacier, lake, catchment, reach, event, hazard_scenario, settlement, exposure, infrastructure, vulnerability, impact, evacuation_origin, safe_zone, route`

Use stable IDs and explicit relationships.

## Phase 04-6 — First real downstream trace

For one glacier/source:

`glacier → source/lake → outlet → reach sequence → downstream settlement`

Produce a trace table containing IDs, geometry lineage, distance, elevation context and confidence/status.

This is the first hard acceptance test of the architecture.

## Phase 04-7 — First event reconstruction

Choose one documented event associated with the pilot.

Separate:

- observed evidence
- interpreted/inferred evidence
- modelled reconstruction

Record event chronology, source evidence, uncertainty and validation targets.

## Phase 04-8 — First hazard scenario

Implement only the process appropriate to the selected pilot event. Do not activate every hazard family merely for completeness.

Outputs should include process-specific footprint/intensity/time variables where defensible.

## Phase 04-9 — First exposure/impact/risk run

Join the validated hazard product with temporally appropriate exposure and documented vulnerability/impact methodology.

Produce component outputs before any composite risk index.

## Phase 04-10 — First evacuation analysis

Construct a QA'd pedestrian/road network for the pilot, identify hazard-affected segments, screen safe-zone candidates and calculate alternative routes. Candidate safe zones remain labelled until field/authority validation.

## Phase 04-11 — First visualization vertical slice

Deliver a working 2D page where a user can:

1. select the pilot glacier/event
2. trace downstream network
3. inspect settlements/exposure
4. toggle hazard/impact/risk
5. inspect evacuation routes
6. open provenance/method details

Then add pilot 3D and time animation.

## Phase 04-12 — Reproducibility and release

Generate:

- data manifest
- processing manifest
- scenario manifest
- software version
- parameter file
- QA report
- validation report
- map/report exports
- release notes

A clean environment must be able to reproduce the pilot outputs from documented inputs.

## Development workflow

Primary development tools:

`Google Colab + Python + GitHub`

AI-assisted coding may use Gemini/AI Studio, but generated code is reviewed and tested before merge/release.

Recommended notebook progression:

`00_environment → 01_registry → 02_ingest → 03_QA → 04_standardize → 05_network_trace → 06_event_reconstruction → 07_hazard → 08_exposure_impact → 09_evacuation → 10_export`

Production logic should be promoted from notebooks into `src/hgscris/` after validation.

## GitHub branch/release discipline

Recommended:

- `main` = reproducible stable branch
- feature branches for implementation
- pull requests for substantial changes
- tagged pilot releases
- CI tests on every PR

Never commit secrets, access tokens or unlicensed restricted datasets.

## Acceptance criteria for BUILD-04 pilot

BUILD-04 is complete only when:

- one real pilot source/event is fully ingested
- source lineage is recorded
- automated QA passes or exceptions are documented
- canonical schemas are populated
- downstream trace is reproducible
- event reconstruction is documented
- one appropriate hazard scenario runs
- exposure and impact outputs are generated with temporal status
- evacuation analysis runs on a QA'd network
- 2D end-to-end interface works
- pilot 3D and animation work
- uncertainty/status are visible
- outputs are reproducible from the repository/configuration

## October delivery strategy

Prioritize one complete vertical slice before broad geographic scaling. After pilot acceptance:

`Pilot → 3–5 events/glacier systems → regional expansion → All-Himalaya inventory/explorer → scalable scenario products`

Do not promise deterministic All-Himalaya risk or evacuation coverage by October. The October target should be a working research platform with defensible pilot analytics and scalable architecture.

## Next execution unit

BUILD-04A — Repository + Environment + Data Directory Audit and implementation baseline.
