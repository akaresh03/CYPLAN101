# Alameda County Accessibility Analysis - Attempt 2

## Project Structure

```
attempt-2/
├── data/
│   ├── bronze/
│   │   └── geometries/          # Raw GeoJSON files from data source
│   ├── silver/
│   │   └── geometries/          # Processed & cleaned geometries
│   └── gold/
│       └── geometries/          # Final analysis-ready data
│
└── src/
    ├── bronze/
    │   └── geometries/
    │       ├── _utilities.py           # Helper functions
    │       └── process_geometries.py   # Convert GeoJSON → GeoParquet
    │
    ├── silver/
    │   └── geometries/
    │       ├── _utilities.py                # Helper functions
    │       ├── address_points.py            # Process address points
    │       ├── census_tract_boundaries.py   # Process census tracts
    │       ├── county_boundary.py           # Process county boundary
    │       ├── street_centerlines.py        # Process street centerlines
    │       └── process_geometries.py        # Master script (auto-runs all)
    │
    └── gold/
        └── geometries/                       # (Future analysis scripts)
```

## Workflow

### Step 1: Bronze Layer - Convert GeoJSON to GeoParquet

```bash
cd src/bronze/geometries
python process_geometries.py
```

This will:
- Read all `.geojson` files from `data/bronze/geometries/`
- Clean filenames (remove numbers, lowercase)
- Convert to GeoParquet format
- Ensure WGS84 (EPSG:4326) projection
- Save back to `data/bronze/geometries/`

**Expected Output:**
```
✓ Processed: Address_Points_...geojson -> address_points.geoparquet
✓ Processed: Census_Tract_Boundaries_...geojson -> census_tract_boundaries.geoparquet
✓ Processed: County_Boundary_...geojson -> county_boundary.geoparquet
✓ Processed: Street_Centerlines_...geojson -> street_centerlines.geoparquet
```

### Step 2: Silver Layer - Process Each Geometry Type

```bash
cd src/silver/geometries
python process_geometries.py
```

This **automatically** finds and runs all processor scripts:
- `address_points.py`
- `census_tract_boundaries.py`
- `county_boundary.py`
- `street_centerlines.py`

Each processor:
- Loads its bronze geoparquet file
- Applies geometry-specific transformations
- Saves to `data/silver/geometries/`

**To add a new geometry type:**
1. Create a new `.py` file (e.g., `parks.py`)
2. Add a `process()` function
3. It will automatically be discovered and run!

### Step 3: Gold Layer - Analysis

(Coming soon - final analysis-ready datasets)

## Key Design Patterns

### Medallion Architecture (Bronze → Silver → Gold)
- **Bronze**: Raw data, minimal processing
- **Silver**: Cleaned, validated, transformed
- **Gold**: Analysis-ready, aggregated, optimized

### Separation of Concerns
- Each geometry type has its own processor file
- Shared utilities in `_utilities.py`
- Master script auto-discovers and runs all processors

### Easy Extensibility
- Add new geometry type = add one new `.py` file with `process()` function
- No need to modify master script

## Running Individual Processors

You can also run processors individually:

```bash
cd src/silver/geometries
python address_points.py
```

## Data Formats

- **Bronze**: GeoParquet (converted from GeoJSON)
- **Silver**: GeoParquet
- **Gold**: GeoParquet (optimized for specific analyses)

**Why GeoParquet?**
- Faster read/write than GeoJSON
- Smaller file sizes
- Preserves spatial metadata
- Standard format for big geospatial data
