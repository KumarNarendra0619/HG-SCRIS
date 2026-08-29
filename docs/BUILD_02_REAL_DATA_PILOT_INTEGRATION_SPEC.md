# BUILD-02 — Real Data & Pilot Event Integration

## Objective
Move HG-SCRIS from module architecture to a reproducible, evidence-led pilot pipeline using real Himalayan datasets and selected historical events.

## Scope
BUILD-02 does NOT attempt to model every Himalayan glacier immediately. It establishes a validated pilot workflow that can later scale glacier-by-glacier.

## Workstreams

### 02A — Data registry
Create a machine-readable registry for every dataset:
- dataset_id
- provider
- product/title
- spatial/temporal coverage
- resolution
- CRS/vertical datum
- access URL/instructions
- licence/usage constraint
- acquisition date
- processing version
- quality status

### 02B — Glacier baseline
Prepare analysis-ready glacier polygons and attributes, including stable identifiers, source date and available mass/elevation/state variables. Do not mix inventories without documented crosswalks.

### 02C — DEM / terrain baseline
Prepare DEM mosaics for pilot areas; verify CRS, vertical datum, resolution, NoData and acquisition date. Preserve raw and conditioned versions separately.

### 02D — Hydrography/connectivity
Integrate rivers, tributaries, lakes, outlets and glacier-to-drainage connectivity. Validate DEM-derived routing against authoritative/mapped hydrography.

### 02E — Settlement/exposure baseline
Build receptor layers for settlements, population and critical infrastructure with source/date/provenance.

### 02F — Event catalogue
For each historical event record:
- event_id
- date/time
- location
- trigger/process class
- source glacier/lake where known
- documented observations
- affected reaches/settlements
- observed damage/footprint
- evidence quality
- references

### 02G — Event reconstruction
Reconstruct selected events using observed evidence first, then run model scenarios. Keep observed and modelled outputs separate for validation.

### 02H — End-to-end pilot
Run:
`Glacier → trigger → cascade → terrain → hazard → exposure → risk/impact → evacuation → 2D/3D/animation`
for selected pilot cases.

## Pilot selection principle
Select a small set of high-information events that span different cascade types (e.g., lake outburst/flood, debris-dominated cascade, compound event) and have sufficient spatial/temporal evidence. The pilot should maximize validation value, not geographic count.

## Data hierarchy
Prefer, in order where available:
1. authoritative government/scientific datasets
2. peer-reviewed/research datasets with clear metadata
3. established global open datasets
4. derived products with documented processing
5. crowdsourced/secondary evidence as supplementary validation

## Data QA gate
No dataset enters modelling until:
- identity/provenance verified
- CRS/datum verified
- geometry/raster integrity checked
- temporal reference recorded
- resolution recorded
- missing/NoData diagnostics completed
- licence/access conditions recorded

## Reproducible processing
Every transformation should record:
`input dataset IDs → processing method → parameters → software/version → output ID → timestamp`

Large raw datasets should not be committed to GitHub. Store access/provenance manifests and small test fixtures in the repository; use external storage or download-at-runtime mechanisms where appropriate.

## Pilot outputs
- analysis-ready glacier/lake layers
- terrain/hydrography network
- event catalogue
- observed event evidence layers
- modelled cascade scenarios
- exposure tables
- risk/impact outputs
- evacuation/safety screening
- 2D/3D visualizations
- validation report
- data/model manifest

## Scientific acceptance criteria
A pilot case is accepted only when:
- data lineage is complete
- connectivity is visually and quantitatively checked
- model assumptions are documented
- observed/modelled layers are separated
- at least one validation comparison is completed
- uncertainty limitations are reported
- no unsupported probability/risk claims are made

## Technology workflow

`Google Colab/Python → analysis artifacts → GitHub/versioning → AI Studio/web integration → deployed research site`

AI-assisted coding may accelerate implementation, but generated code and model outputs require automated tests, data QA and researcher review.

## October target
By October, the goal is a working end-to-end pilot site with reproducible data ingestion and event reconstruction, not unsupported full-Himalaya operational coverage.

## Next build
BUILD-02A — Data Registry & Provenance Loader.
