from seabird_sampling.cli import cli
from geci_test_tools import if_exist_remove, assert_exist
from typer.testing import CliRunner

import os

runner = CliRunner()


def test_cli_plot_distribution_map_reserve():
    output_path = "tests/data/mapa_distribution_reserve.png"
    if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "plot-distribution-map",
            "--data-path",
            "tests/data/nidos_busqueda_aves_marinas_tests.csv",
            "--input-data-type",
            "Burrows",
            "--coast-line-path",
            "tests/data/linea_costa_isla_guadalupe.shp",
            "--islet",
            "Reserva",
            "--species",
            "Phoebastria immutabilis",
            "--season",
            "2018",
            "--wind-rose-path",
            "tests/data/rosewind.png",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert_exist(output_path)
    # os.remove(output_path)


def test_cli_plot_distribution_map():
    result = runner.invoke(
        cli,
        ["plot-distribution-map", "--help"],
    )
    assert "[default: data/raw/rosewind.png]" in result.stdout
    assert " data/raw/linea_costa_isla_guadalupe.shp]" in result.stdout
    assert ' "Yes"}]' in result.stdout
    assert result.exit_code == 0

    output_path = "tests/data/mapa_distribution.png"
    if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "plot-distribution-map",
            "--data-path",
            "tests/data/nidos_busqueda_aves_marinas_tests.csv",
            "--input-data-type",
            "Burrows",
            "--coast-line-path",
            "tests/data/linea_costa_isla_guadalupe.shp",
            "--islet",
            "Morro Prieto",
            "--species",
            "Phoebastria immutabilis",
            "--season",
            "2018",
            "--wind-rose-path",
            "tests/data/rosewind.png",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert_exist(output_path)
    os.remove(output_path)


def test_cli_plot_density_map():
    result = runner.invoke(
        cli,
        ["plot-density-map", "--help"],
    )
    assert "[default: data/raw/rosewind.png]" in result.stdout
    assert " data/raw/linea_costa_isla_guadalupe.shp]" in result.stdout
    assert ' "No"}]' in result.stdout
    assert result.exit_code == 0

    output_path = "tests/data/mapa.png"
    if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "plot-density-map",
            "--data-path",
            "tests/data/nidos_busqueda_aves_marinas_tests.csv",
            "--input-data-type",
            "Burrows",
            "--coast-line-path",
            "tests/data/linea_costa_isla_guadalupe.shp",
            "--islet",
            "Morro Prieto",
            "--species",
            "Phoebastria immutabilis",
            "--season",
            "2018",
            "--wind-rose-path",
            "tests/data/rosewind.png",
            "--points-option",
            '{"Show Points": "No"}',
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert_exist(output_path)
    os.remove(output_path)


def test_cli_write_burrows_count_by_season():
    result = runner.invoke(
        cli,
        ["write-burrows-count-by-season", "--help"],
    )

    assert " Burrows data path " in result.stdout
    assert " Species to count " in result.stdout
    assert " Colony to count " in result.stdout
    assert " Output path " in result.stdout
    assert result.exit_code == 0

    output_path = "tests/data/total_burrows_gumu_punta_sur.csv"
    result = runner.invoke(
        cli,
        [
            "write-burrows-count-by-season",
            "--data-path",
            "tests/data/nidos_busqueda_aves_marinas_tests.csv",
            "--species",
            "Synthliboramphus hypoleucus",
            "--colony",
            "Punta Sur",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)


def test_cli_version():
    result = runner.invoke(
        cli,
        ["version", "--help"],
    )
    assert result.exit_code == 0


def test_cli_concatename_burrows_by_season():
    result = runner.invoke(
        cli,
        ["concatenate-burrows-by-season", "--help"],
    )
    assert result.exit_code == 0
    assert " First colony data path " in result.stdout
    assert " Second colony data path " in result.stdout
    assert " Output path " in result.stdout
    assert result.exit_code == 0

    output_path = "tests/data/concatenated_total_nidos.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = runner.invoke(
        cli,
        [
            "concatenate-burrows-by-season",
            "--first-colony-path",
            "tests/data/total_nidos_temporada_mergulo_punta_sur.csv",
            "--second-colony-path",
            "tests/data/total_nidos_temporada_petrel_morro_prieto.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)


def test_cli_concatenate_burrows_by_season_to_cantidad_nidos():
    result = runner.invoke(
        cli,
        ["concatenate-burrows-by-season-to-cantidad-nidos", "--help"],
    )
    assert result.exit_code == 0
    assert " First colony data path " in result.stdout
    assert " Second colony data path " in result.stdout
    assert " Output path " in result.stdout
    assert result.exit_code == 0

    output_path = "tests/data/concatenated_cantidad_nidos.csv"

    if os.path.exists(output_path):
        os.remove(output_path)

    result = runner.invoke(
        cli,
        [
            "concatenate-burrows-by-season-to-cantidad-nidos",
            "--first-colony-path",
            "tests/data/total_nidos_temporada_mergulo_punta_sur.csv",
            "--second-colony-path",
            "tests/data/total_nidos_temporada_petrel_morro_prieto.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    assert os.path.exists(output_path)
