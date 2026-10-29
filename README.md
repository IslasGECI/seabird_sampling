<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# Seabird sampling
[![codecov](https://codecov.io/gh/IslasGECI/seabird_sampling/graph/badge.svg?token=RY807ST1T1)](https://codecov.io/gh/IslasGECI/seabird_sampling)
![example branch
parameter](https://github.com/IslasGECI/seabird_sampling/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/seabird_sampling)
![languages](https://img.shields.io/github/languages/top/IslasGECI/seabird_sampling)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/seabird_sampling)
![PyPI - Version](https://img.shields.io/pypi/v/seabird_sampling)

Turn seabird burrow and nest observations into maps and seasonal summaries.

## What it does

`seabird_sampling` helps field teams and analysts:

- Create distribution and burrow-density maps for a species, islet, and season.
- Combine colony records into a single table.
- Count burrows by season and prepare historical totals.

The same features are available through the `seabird-sampling` command, also
available as `muestreo-aves-marinas-ipbc`.

## Usage

List the available commands:

```bash
seabird-sampling --help
```

Create a distribution map:

```bash
seabird-sampling plot-distribution-map \
  --data-path path/to/burrows.csv \
  --input-data-type Burrows \
  --islet "Morro Prieto" \
  --species "Phoebastria immutabilis" \
  --season 2018 \
  --output-path output/distribution.png
```

| Command | Options | Purpose |
| --- | --- | --- |
| `plot-distribution-map` | `--data-path`, `--input-data-type`, `--coast-line-path`, `--islet`, `--species`, `--season`, `--wind-rose-path`, `--points-option`, `--output-path` | Plot a distribution map for a species, islet, and season. |
| `plot-density-map` | `--data-path`, `--input-data-type`, `--coast-line-path`, `--islet`, `--species`, `--season`, `--wind-rose-path`, `--points-option`, `--output-path` | Plot a burrow density map for a species, islet, and season. |
| `concatenate-burrows-by-season` | `--first-colony-path`, `--second-colony-path`, `--output-path` | Concatenate two colony datasets into one CSV file. |
| `concatenate-burrows-by-season-to-cantidad-nidos` | `--first-colony-path`, `--second-colony-path`, `--output-path` | Concatenate two colony datasets using the total-burrow format. |
| `write-burrows-count-by-season` | `--data-path`, `--species`, `--colony`, `--output-path` | Write the total burrow count per season for a species and colony. |
| `write-historical-burrows-by-species-and-island` | `--data-path`, `--species`, `--colony`, `--output-path` | Write historical burrow counts filtered by species and colony. |
| `version` | None | Print the package version. |

Run any command with `--help` to see all options and their defaults.

## Before you start

- Install Python 3.10 or newer.
- Provide observation data as CSV files.
- For maps, provide a coastline shapefile and a wind-rose image.
- Map commands look for the coastline and wind rose under `data/raw/` unless
  `--coast-line-path` and `--wind-rose-path` are supplied.

## Run the project

### Docker (recommended)

Build the image and run the command inside it:

```bash
docker compose build
docker compose run --rm islasgeci seabird-sampling --help
```

### Native

Install from PyPI and run the command directly:

```bash
pip install seabird_sampling
seabird-sampling --help
```

For development setup and checks, see `AGENTS.md`.
