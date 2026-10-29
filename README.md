<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# Seabird sampling
[![codecov](https://codecov.io/gh/IslasGECI/seabird_sampling/graph/badge.svg?token=RY807ST1T1)](https://codecov.io/gh/IslasGECI/seabird_sampling)
![example branch
parameter](https://github.com/IslasGECI/seabird_sampling/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/seabird_sampling)
![languages](https://img.shields.io/github/languages/top/IslasGECI/seabird_sampling)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/seabird_sampling)
![PyPI - Version](https://img.shields.io/pypi/v/seabird_sampling)

Python module to process data from seabird sampling.

`seabird_sampling` provides tools for cleaning, filtering, summarising, and
visualising seabird burrow and nest data. It includes density and distribution
maps, per-season burrow counts, historical data adaptation, and a command-line
interface exposed as `seabird-sampling` (or `muestreo-aves-marinas-ipbc`).

## Quickstart

### Install

Install the package from PyPI:

```bash
pip install seabird_sampling
```

For development, install an editable copy from a repository checkout:

```bash
pip install --editable .
```

This installs the `seabird-sampling` command. The alias
`muestreo-aves-marinas-ipbc` is also available.

### Use

List the available commands and print the version:

```bash
seabird-sampling --help
seabird-sampling version
```

Generate a distribution map:

```bash
seabird-sampling plot-distribution-map \
  --data-path path/to/burrows.csv \
  --input-data-type Burrows \
  --islet "Morro Prieto" \
  --species "Phoebastria immutabilis" \
  --season 2018 \
  --output-path output/distribution.png
```

The coastline and wind-rose paths default to the files under `data/raw/`.
Override them with `--coast-line-path` and `--wind-rose-path` when needed.
Run any command with `--help` to see all options and their defaults.

## Command-line interface

| Function | Command | Options | Purpose |
| --- | --- | --- | --- |
| `plot_distribution_map` | `plot-distribution-map` | `--data-path`, `--input-data-type`, `--coast-line-path`, `--islet`, `--species`, `--season`, `--wind-rose-path`, `--points-option`, `--output-path` | Plot a distribution map for a species, islet, and season. |
| `plot_density_map` | `plot-density-map` | `--data-path`, `--input-data-type`, `--coast-line-path`, `--islet`, `--species`, `--season`, `--wind-rose-path`, `--points-option`, `--output-path` | Plot a burrow density map for a species, islet, and season. |
| `concatenate_burrows_by_season` | `concatenate-burrows-by-season` | `--first-colony-path`, `--second-colony-path`, `--output-path` | Concatenate two colony datasets into one CSV file. |
| `concatenate_burrows_by_season_to_cantidad_nidos` | `concatenate-burrows-by-season-to-cantidad-nidos` | `--first-colony-path`, `--second-colony-path`, `--output-path` | Concatenate two colony datasets using the total-burrow format. |
| `write_burrows_count_by_season` | `write-burrows-count-by-season` | `--data-path`, `--species`, `--colony`, `--output-path` | Write the total burrow count per season for a species and colony. |
| `write_historical_burrows_by_species_and_island` | `write-historical-burrows-by-species-and-island` | `--data-path`, `--species`, `--colony`, `--output-path` | Write historical burrow counts filtered by species and colony. |
| `version` | `version` | None | Print the package version. |
