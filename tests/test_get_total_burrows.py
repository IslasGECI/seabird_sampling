import pandas as pd
from muestreo_aves_marinas_ipbc import (
    get_total_burrows,
    get_cantidad_nidos,
    concatenate_colonies,
    concatenate_main_islet_colonies,
)


def test_get_total_burrows():
    mergulo_zapato_burrows = pd.read_csv("tests/data/serie_tiempo_mergulo_zapato.csv")
    mergulo_punta_sur_burrows = pd.read_csv(
        "tests/data/total_nidos_temporada_mergulo_punta_sur.csv"
    )
    obtained = get_total_burrows(mergulo_zapato_burrows, mergulo_punta_sur_burrows)
    obtained_burrows_2017 = obtained.loc[2017, "Cantidad de nidos"]
    expected_burrows_2017 = 1760
    assert obtained_burrows_2017 == expected_burrows_2017


def test_get_cantidad_nidos():
    mergulo_zapato_burrows = pd.read_csv("tests/data/serie_tiempo_mergulo_zapato.csv")
    path_punta_sur_data = "tests/data/total_nidos_temporada_mergulo_punta_sur.csv"
    obtained = get_cantidad_nidos(
        mergulo_zapato_burrows, mergulo_zapato_burrows, path_punta_sur_data, "All islets"
    )
    obtained_burrows_2017 = obtained.loc[2017, "Cantidad de nidos"]
    expected_burrows_2017 = 1720 * 2 + 40
    assert obtained_burrows_2017 == expected_burrows_2017

    mergulo_zapato_burrows = pd.read_csv("tests/data/serie_tiempo_mergulo_zapato.csv")
    obtained = get_cantidad_nidos(
        mergulo_zapato_burrows, mergulo_zapato_burrows, path_punta_sur_data, "Mergulo y Zapato"
    )
    obtained_burrows_2017 = obtained.loc[2017, "Cantidad de nidos"]
    expected_burrows_2017 = 1720 * 2
    assert obtained_burrows_2017 == expected_burrows_2017, "Mergulo y Zapato"
    obtained_columns = obtained.columns
    expected_columns = ["Temporada", "Cantidad de nidos"]
    assert (obtained_columns == expected_columns).all(), "Have the same columns"


def test_concatenate_main_islet_colonies():
    main_islet = _build_a_colony([1, 2, 3], [2, 4, 6])
    punta_sur = _build_a_colony([1, 3], [3, 9])
    obtained = concatenate_main_islet_colonies(main_islet, punta_sur)
    expected_n_row = 3
    obtained_n_row = len(obtained)
    assert obtained_n_row == expected_n_row

    obtained_first_season = obtained.loc[1].Total_nidos
    expected_first_season = 2 + 3
    assert obtained_first_season == expected_first_season


def test_concatenate_colonies():
    morro_nests = _build_a_colony([2014, 2015, 2020], [10, 20, 30])
    zapato_nests = _build_a_colony([2015, 2020], [200, 300])
    obtained = concatenate_colonies(zapato_nests, morro_nests)
    print(obtained)
    assert obtained.index[0] == 2014


def _build_a_colony(temporada: list, total_nidos: list):
    return pd.DataFrame({"Temporada": temporada, "Total_nidos": total_nidos})
