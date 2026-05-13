from seabird_sampling.plot_error_bar import (
    get_table_salida,
    make_sure_folder_exists,
    plot_breeding_pairs_with_error_bars,
)

import matplotlib as plt
import os
import numpy as np
import pandas as pd
import shutil


def tests_plot_breeding_pairs_with_error_bars():
    plot_path = "tests/data/breeding_pairs_with_errorbars.png"

    datos_madrigueras_kernel = pd.read_csv("tests/data/datos_madrigueras_kernel_tests.csv")
    temporadas = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2022"]
    serie_kernel = [
        292.50553716,
        382.37169617,
        1753.27114144,
        1036.10395092,
        563.86609574,
        896.14433073,
        757.19161428,
        1130.95428345,
    ]
    obtained = plot_breeding_pairs_with_error_bars(
        plot_path, datos_madrigueras_kernel, temporadas, serie_kernel
    )

    assert isinstance(obtained, plt.axes._axes.Axes)

    obtained_y_label = obtained.get_ylabel()
    assert obtained_y_label == "Total of breeding pairs"

    obtained_number_error_bars = len(obtained.get_lines()[0].get_xdata())
    expected_number_error_bars = len(datos_madrigueras_kernel)
    assert obtained_number_error_bars == expected_number_error_bars

    obtained_length_time_series = len(obtained.get_lines()[1].get_xdata())
    expected_length_time_series = len(temporadas)
    assert obtained_length_time_series == expected_length_time_series


def test_make_sure_folder_exist():
    folder = "tests/prueba"
    assert not os.path.exists(folder), "Make sure folde does not exist"
    make_sure_folder_exists(folder)
    assert os.path.exists(folder)
    shutil.rmtree(folder)


def test_get_table_salida():
    temporadas = np.array(["2000", "2010", "1999"])
    serie_kernel = np.array([2000.2000, 2010.2010, 1999.1999])

    obtained = get_table_salida(temporadas, serie_kernel)
    assert obtained["Cantidad de nidos"][1] == 2010.2010
    assert obtained["Temporada"][2] == "1999"
