# Public Interface

### cli plot-distribution-map --data-path --input-data-type --coast-line-path --islet --species --season --wind-rose-path --points-option --output-path
Plot and save a distribution map for a species, islet, and season.

**Parameters:**
- `--data-path`: Path to the burrow or quadrant observation CSV.
- `--input-data-type`: Input data type, such as `Burrows` or `Quadrants`.
- `--coast-line-path`: Coastline shapefile path. Defaults to `data/raw/linea_costa_isla_guadalupe.shp`.
- `--islet`: Islet or colony name.
- `--species`: Species scientific name.
- `--season`: Season year.
- `--wind-rose-path`: Wind-rose image path. Defaults to `data/raw/rosewind.png`.
- `--points-option`: JSON object controlling point display. Defaults to `{"Show Points": "Yes"}`.
- `--output-path`: Destination image path.

**Returns:** None; writes the map image.

### cli plot-density-map --data-path --input-data-type --coast-line-path --islet --species --season --wind-rose-path --points-option --output-path
Plot and save a burrow density map for a species, islet, and season.

**Parameters:**
- `--data-path`: Path to the burrow or quadrant observation CSV.
- `--input-data-type`: Input data type, such as `Burrows` or `Quadrants`.
- `--coast-line-path`: Coastline shapefile path. Defaults to `data/raw/linea_costa_isla_guadalupe.shp`.
- `--islet`: Islet or colony name.
- `--species`: Species scientific name.
- `--season`: Season year.
- `--wind-rose-path`: Wind-rose image path. Defaults to `data/raw/rosewind.png`.
- `--points-option`: JSON object controlling point display. Defaults to `{"Show Points": "No"}`.
- `--output-path`: Destination image path.

**Returns:** None; writes the map image.

### cli concatenate-burrows-by-season --first-colony-path --second-colony-path --output-path
Concatenate two colony datasets into one CSV file.

**Parameters:**
- `--first-colony-path`: First colony CSV path.
- `--second-colony-path`: Second colony CSV path.
- `--output-path`: Destination CSV path.

**Returns:** None; writes a CSV with `Temporada` and `Total_nidos`.

### cli concatenate-burrows-by-season-to-cantidad-nidos --first-colony-path --second-colony-path --output-path
Concatenate two colony datasets using the total-burrow format.

**Parameters:**
- `--first-colony-path`: First colony CSV path.
- `--second-colony-path`: Second colony CSV path.
- `--output-path`: Destination CSV path.

**Returns:** None; writes a CSV with `Cantidad de nidos` and `Temporada`.

### cli write-burrows-count-by-season --data-path --species --colony --output-path
Write the total burrow count per season for a species and colony.

**Parameters:**
- `--data-path`: Burrow observation CSV path.
- `--species`: Species to count.
- `--colony`: Colony to count.
- `--output-path`: Destination CSV path.

**Returns:** None; writes a CSV containing `Total_nidos` by season.

### cli write-historical-burrows-by-species-and-island --data-path --species --colony --output-path
Write historical burrow counts filtered by species and colony.

**Parameters:**
- `--data-path`: Historical observation CSV path.
- `--species`: Species to count.
- `--colony`: Colony to count.
- `--output-path`: Destination CSV path.

**Returns:** None; writes a CSV containing `Temporada` and `Total_nidos`.

### cli version
Print the installed package version.

**Returns:** None; prints the version to standard output.

### write_error_bars_json(barras_error_df, ruta_intervalo_error)
Write error-bar seasons and bounds to a JSON file.

**Parameters:**
- `barras_error_df`: DataFrame with `temporada`, `minimo`, and `maximo` columns.
- `ruta_intervalo_error`: Destination JSON path.

**Returns:** None.

**Notes:** Creates `reports/non-tabular` before writing the file.

### BurrowSeries(exhaustive_data, central_and_deltas_densities, kernel_area)
Build a combined burrow series from exhaustive counts and sampled density estimates.

**Parameters:**
- `exhaustive_data`: DataFrame with `Temporada` and `Total_nidos` columns.
- `central_and_deltas_densities`: DataFrame with `temporada`, `central`, `minimo`, and `maximo` columns.
- `kernel_area`: Mapping with an `area` value used to scale density estimates.

**Returns:** A `BurrowSeries` instance.

**Notes:** Provides `get_error_deltas()` and `get_table_of_central_values()`. Sampling deltas are scaled by `kernel_area["area"]`; a correction factor is applied when 2018 sampling data is present.

### add_intervals_to_sampled_season(barras_error_df, results)
Combine sampled-season error bars with exhaustive counts.

**Parameters:**
- `barras_error_df`: DataFrame with `temporada`, `minimo`, and `maximo` columns.
- `results`: DataFrame with `Temporada` and `Cantidad de nidos` columns.

**Returns:** A DataFrame with `Temporada`, `Cantidad de nidos`, and `percentage_error`.

### get_intervals_from_error_bars_and_series(barras_error_df, cantidad_nidos)
Merge error bars with the central burrow series.

**Parameters:**
- `barras_error_df`: DataFrame with `temporada`, `minimo`, and `maximo` columns.
- `cantidad_nidos`: DataFrame with `Temporada` and `Cantidad de nidos` columns.

**Returns:** A DataFrame with `temporada`, `minimo`, `maximo`, and `central` columns.

### get_latitude_from_kml(kml_features)
Extract latitudes from the first KML feature's exterior coordinates.

**Parameters:**
- `kml_features`: List of KML features.

**Returns:** A NumPy array of latitudes.

### get_longitude_from_kml(kml_features)
Extract longitudes from the first KML feature's exterior coordinates.

**Parameters:**
- `kml_features`: List of KML features.

**Returns:** A NumPy array of longitudes.

### read_kml_features(kml_file)
Read KML features from a file.

**Parameters:**
- `kml_file`: Path to a KML file.

**Returns:** A list of features from the first KML document feature.

### Plotter_Burrows(paths, plot_density=True)
Draw and save burrow maps.

**Parameters:**
- `paths`: `GeciCliOptions`-compatible object with wind-rose, point-display, and output paths.
- `plot_density`: Whether to draw the density layer and color bar.

**Returns:** A `Plotter_Burrows` instance.

**Notes:** The constructor opens and resizes the wind-rose image and parses the points option JSON.

### get_cantidad_nidos(datos_nidos_morro, datos_nidos_zapato, ruta_datos_punta_sur, option_only_islets)
Combine colony counts, optionally adding Punta Sur data.

**Parameters:**
- `datos_nidos_morro`: First colony DataFrame with `Cantidad de nidos`.
- `datos_nidos_zapato`: Second colony DataFrame with `Cantidad de nidos`.
- `ruta_datos_punta_sur`: CSV path used when including all islets.
- `option_only_islets`: Set to `All islets` to include Punta Sur data.

**Returns:** A DataFrame with `Cantidad de nidos` and `Temporada`; otherwise a DataFrame indexed by `Temporada`.

### max_min_from_dataframe(dataframe)
Build an error-bar array from minimum and maximum columns.

**Parameters:**
- `dataframe`: DataFrame with `minimo` and `maximo` columns.

**Returns:** A NumPy array containing the minimum and maximum series.

### combine_error_bars(error_morro, error_zapato)
Add two colony error-bar tables by season.

**Parameters:**
- `error_morro`: First error-bar data with `temporada`, `minimo`, and `maximo`.
- `error_zapato`: Second error-bar data with `temporada`, `minimo`, and `maximo`.

**Returns:** A DataFrame with combined `temporada`, `minimo`, and `maximo` values.

### get_table_salida(temporadas, serie_kernel)
Build the output table used by error-bar plots.

**Parameters:**
- `temporadas`: Season labels.
- `serie_kernel`: Burrow series values.

**Returns:** A dictionary with `Temporada` and `Cantidad de nidos` lists.

### make_sure_folder_exists(folder)
Create a folder when it does not exist.

**Parameters:**
- `folder`: Folder path.

**Returns:** None.

### plot_error_bars(exhaustive_data, output_path)
Plot error bars in black.

**Parameters:**
- `ax`: A `matplotlib.axes.Axes.axis` instance to add the error bars.
- `x`: An iterable with the same length as `y`.
- `y`: A DataFrame with columns `minimo`, `maximo` and `central`.

**Returns:** None.

**Notes:** Saves the figure at 300 dpi.

### plot_exhaustive_searches(exhaustive_data, output_path)
Plot exhaustive breeding-pair counts by season and save the figure.

**Parameters:**
- `exhaustive_data`: DataFrame with `Temporada` and `Total_nidos` columns.
- `output_path`: Destination image path.

**Returns:** None.

**Notes:** Saves the figure at 300 dpi.
