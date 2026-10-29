# Agent Guidelines

## Public interface

The public interface is the CLI commands registered on `seabird_sampling.cli.cli`
and exposed as `seabird-sampling` and `muestreo-aves-marinas-ipbc` through
`[tool.flit.scripts]` in `pyproject.toml`. Treat internal package functions as
developer-only unless the interface definition changes.

## Developer commands

- `make check` runs Black (`--line-length 100`), Flake8, and mypy on both the module and tests.
- `make tests` runs `pytest --verbose tests`; `make coverage` installs the package before running coverage.
- `make mutants` runs `mutmut` using `paths_to_mutate = ["seabird_sampling/"]` from `pyproject.toml`.
- `make all` runs `check`, `coverage`, then `mutants`.
- CI builds the Docker image, runs `make check`, `make coverage`, and `make mutants`, then publishes to PyPI on pushes to `develop`.

## Conventions

- Black and Flake8 use line length 100. Flake8 ignores E203, E266, E501, and W503; maximum complexity is 18.
- CLI commands use Typer. Function names map to hyphenated commands, such as `plot_distribution_map` to `plot-distribution-map`.
- Typer displays command docstrings in `--help`; keep them user-facing.
- The `version` command reads `seabird_sampling.__version__` from `seabird_sampling/__init__.py`. Keep it in sync with `CHANGELOG.md`.
- Map commands default to `data/raw/linea_costa_isla_guadalupe.shp` and `data/raw/rosewind.png`.
- CLI tests use `typer.testing.CliRunner` and write generated files into `tests/data/`.

## Verification

- Use the Docker image when the host lacks the test toolchain; its Dockerfile installs Black, Flake8, mutmut, mypy, pylint, pytest, and pytest-cov.
- There is no dependency lockfile or requirements file; dependencies and mypy overrides live in `pyproject.toml`.
