# Testing Guide for OSMnx Pipeline

## Quick Fix Summary

**Problem:** The notebook was using relative paths that didn't work when running from the `notebooks/` directory.

**Solution:** Updated [config.py](src/osmnx_pipeline/config.py) to use absolute paths based on the project root directory.

---

## How to Test the Pipeline

### Option 1: Quick Configuration Test (Recommended First)

Run this to verify all paths and imports work correctly:

```bash
# Activate your conda environment
conda activate cyplan-101-env

# Run the test script from project root
python test_config.py
```

This will verify:
- ✓ All file paths exist and are accessible
- ✓ GeoPandas can load all geometry files
- ✓ All pipeline modules import correctly
- ✓ `load_study_area()` function works

**Expected output:** All checkmarks (✓) with no errors.

---

### Option 2: Full Pipeline Test (Comprehensive)

Once the quick test passes, run the full notebook:

```bash
# Navigate to notebooks directory
cd notebooks

# Launch Jupyter
jupyter notebook test.ipynb
```

Then **run cells sequentially** (Shift+Enter) to test:

1. **Setup** - Import all libraries
2. **Load Geometries** - Verify gold layer data
3. **Build Network** - Download OSM walk network (5-15 min)
4. **Fetch Amenities** - Download POIs from OSM
5. **Calculate Distances** - Run proximity analysis
6. **Visualizations** - Generate maps and plots
7. **Export Results** - Save outputs to `data/test_outputs/`

**Estimated Runtime:**
- Quick tests (cells 1-2): ~1 minute
- Network building (cell 3): 5-15 minutes
- Distance calculations (cells 7-9): 10-30 minutes
- Total: ~20-45 minutes for full pipeline

---

## What Changed

### Before (Broken):
```python
# config.py
ADDR_PATH = "data/gold/geometries/address_points.geoparquet"  # Relative path
```

This only worked when running from project root, not from `notebooks/`.

### After (Fixed):
```python
# config.py
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
ADDR_PATH = PROJECT_ROOT / "data" / "gold" / "geometries" / "address_points.geoparquet"
```

Now works from **any directory** in the project.

---

## Troubleshooting

### Issue: ModuleNotFoundError for geopandas/osmnx

**Solution:** Make sure you're in the conda environment:
```bash
conda activate cyplan-101-env
python -c "import geopandas; print('✓ geopandas installed')"
```

### Issue: FileNotFoundError even after fix

**Solution:** Verify files exist:
```bash
ls -lh data/gold/geometries/
```

Should show:
- `address_points.geoparquet` (~55 MB)
- `county_boundary.geoparquet` (~77 KB)
- `census_tract_boundaries.geoparquet` (~2.1 MB)

### Issue: Network building times out

**Solution:**
1. Check internet connection
2. Try a smaller area first (modify study area)
3. Increase OSMnx timeout (default is 180s)

---

## Running Individual Tests

You can test specific functions independently:

### Test 1: Load Study Area
```python
from osmnx_pipeline.network import load_study_area
study_area = load_study_area()
print(study_area.geom_type)  # Should print "Polygon" or "MultiPolygon"
```

### Test 2: Fetch Amenities
```python
from osmnx_pipeline.amenities import fetch_amenities
bus_stops = fetch_amenities("bus_stops")
print(f"Found {len(bus_stops)} bus stops")
```

### Test 3: Build Network (takes time!)
```python
from osmnx_pipeline.network import build_walk_network
G = build_walk_network()
print(f"Network has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
```

---

## Expected Outputs

After running the full notebook, you should have:

### Console Output:
- Network statistics (nodes, edges, connectivity)
- Amenity counts for each type
- Distance statistics (mean, median, percentiles)
- Summary table comparing all amenity types

### Visualizations:
- Study area map
- Network sample visualization
- Amenity location maps (5 types)
- Distance distribution plots
- Comparative bar charts and box plots

### Files Created:
```
data/test_outputs/
├── amenity_distance_summary.csv          # Summary statistics table
├── bus_stops_distances.geoparquet        # Full results with geometry
└── bus_stops_distances_sample.csv        # 1000 row sample
```

---

## Next Steps After Testing

Once all tests pass:

1. **Add more amenity types** to `config.OSM_TAGS_HIGH`
2. **Add travel time calculations** (distance / walking speed)
3. **Aggregate to census tracts** for equity analysis
4. **Scale up** to run on full county or multiple cities
5. **Add demographic overlays** for equity metrics

---

## Performance Notes

**Current Scale:**
- 634,217 address points
- 5 amenity types
- Walking network only

**Memory Usage:**
- Network building: ~1-2 GB
- Distance calculation: ~2-3 GB
- Keep other applications closed for large analyses

**Parallelization Options:**
- Process cities separately, then merge
- Use multiprocessing for multiple amenity types
- Consider Pandana for faster routing (alternative to NetworkX)

---

## Contact

Questions about the pipeline? Check:
- Main documentation: [README.md](attempt-1/README.md)
- Getting started guide: [attempt-1/GETTING_STARTED.md](attempt-1/GETTING_STARTED.md)
- Project proposal: See project notes in this document

---

**Happy testing!** 🗺️ 📊
