from muestreo_aves_marinas_ipbc import write_error_bars_json, BurrowSeries
from geci_test_tools import if_exist_remove, assert_exist

import json
import numpy as np
import pandas as pd
import pytest


def tests_BurrowsIntervals_get_error_deltas():
    exahustive_data = pd.DataFrame({"Temporada": [2001, 2002, 2003], "Total_nidos": [1, 2, 3]})
    central_and_deltas_densities_without_2002 = pd.DataFrame(
        {"temporada": [2001, 2003], "central": [3, 4], "minimo": [1, 2], "maximo": [5, 6]}
    )

    area_kernel = {"area": 100}
    obtained_burrows_object = BurrowSeries(
        exahustive_data, central_and_deltas_densities_without_2002, area_kernel
    )
    obtained_error_deltas = obtained_burrows_object.get_error_deltas()
    obtained_shape_error_deltas = obtained_error_deltas.shape
    expected_shape_error_deltas = (2, 3)
    assert obtained_shape_error_deltas == expected_shape_error_deltas

    assert obtained_shape_error_deltas == expected_shape_error_deltas
    obtained_error_deltas = obtained_burrows_object.get_error_deltas()
    expected_columns = set(["temporada", "minimo", "maximo"])
    assert set(obtained_error_deltas.columns) == expected_columns


def tests_BurrowsIntervals():
    exahustive_data = pd.read_csv("tests/data/total_nidos_temporada_petrel_morro_prieto.csv")
    central_and_deltas_densities_without_2018 = pd.read_csv(
        "tests/data/intervalo_densidad_petrel_morro_with_2021.csv"
    )
    path_area_kernel_morro = "tests/data/area_morro_prieto_kernel_petrel_2019.json"
    with open(path_area_kernel_morro, encoding="utf8") as area_json:
        area_kernel_morro = json.load(area_json)

    obtained_object = BurrowSeries(
        exahustive_data, central_and_deltas_densities_without_2018, area_kernel_morro
    )
    expected_nidos_2018 = 320
    assert obtained_object.nidos_2018 == expected_nidos_2018

    obtained_interval_burrows = obtained_object.burrows_central_and_deltas
    expected_interval_burrows_columns = ["temporada", "central", "minimo", "maximo"]
    assert (obtained_interval_burrows.columns == expected_interval_burrows_columns).all()

    obtained_proportion_kernel = obtained_object.correction_factor
    expected_proportion_kernel = 1.762
    assert pytest.approx(obtained_proportion_kernel, rel=1e-3) == expected_proportion_kernel

    obtained_seasons = obtained_object.seasons
    expected_seasons = np.array(np.arange(2014, 2023), dtype=str)
    assert (obtained_seasons == expected_seasons).all()

    obtained_serie = obtained_object.serie_of_central_values
    expected_length = 9
    obtained_length = len(obtained_serie)
    assert obtained_length == expected_length

    obtained_table_of_central_values = obtained_object.get_table_of_central_values()
    assert (
        pytest.approx(obtained_table_of_central_values["Cantidad de nidos"].iloc[0], rel=1e-3)
        == 292.5
    )
    print(obtained_table_of_central_values)
    assert len(obtained_table_of_central_values.columns) == 2
    assert obtained_table_of_central_values["Temporada"].iloc[6] == 2020

    central_and_deltas_densities_without_2018 = pd.read_csv(
        "tests/data/intervalo_densidad_without_2018.csv"
    )
    obtained_object = BurrowSeries(
        exahustive_data, central_and_deltas_densities_without_2018, area_kernel_morro
    )

    obtained_proportion_kernel = obtained_object._calculate_correction_factor()
    expected_proportion_kernel = 1
    assert obtained_proportion_kernel == expected_proportion_kernel

    under_estimated_central_and_deltas_densities = pd.DataFrame(
        {"temporada": [2018], "central": [0.0042], "minimo": [0.0017], "maximo": [0.002]}
    )
    census_data = pd.DataFrame({"Temporada": [2018], "Total_nidos": [297]})
    obtained_object = BurrowSeries(
        census_data, under_estimated_central_and_deltas_densities, area_kernel_morro
    )

    obtained_proportion_kernel = obtained_object._calculate_correction_factor()
    expected_proportion_kernel = 1
    assert obtained_proportion_kernel == expected_proportion_kernel


def tests_write_error_bars_json():
    error_bars_from_kernel_df = pd.DataFrame(
        {
            "temporada": [2018, 2019, 2020, 2021, 2022],
            "minimo": [136.93890897, 449.07906911, 201.38074848, 397.92835899, 397.92835899],
            "central": [140, 460, 210, 480, 480],
            "maximo": [161.10459878, 505.46567868, 221.51882333, 519.50594446, 519.50594446],
        }
    )
    output_path = "tests/data/error_bars_ouput.json"
    if_exist_remove(output_path)
    write_error_bars_json(error_bars_from_kernel_df, output_path)
    assert_exist(output_path)
    with open(output_path, encoding="utf8") as json_error:
        error_bars_from_kernel = json.load(json_error)
    assert list(error_bars_from_kernel.keys()) == ["temporada", "minimo", "maximo"]
