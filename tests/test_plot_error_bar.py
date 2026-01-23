from seabird_sampling.plot_error_bar import (
    get_table_salida,
    make_sure_folder_exists,
    plot_breeding_pairs_with_error_bars,
)

import hashlib
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
    plot_breeding_pairs_with_error_bars(
        plot_path, datos_madrigueras_kernel, temporadas, serie_kernel
    )
    expected_hash = "978bbe536259e45a6dce3c69c59c6112"
    figure_content = open(plot_path, "rb").read()
    obtained_hash = hashlib.md5(figure_content).hexdigest()
    assert obtained_hash == expected_hash
    os.remove(plot_path)


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
