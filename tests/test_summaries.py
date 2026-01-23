from seabird_sampling.summaries import Summary_Constructor

import pandas as pd


def test_build_density_summary():
    burrows_data = pd.read_csv("tests/data/madrigueras_cuadrantes_avesmarinas_test.csv")
    summary = Summary_Constructor(burrows_data)
    islet = "Morro Prieto"
    specie = "Synthliboramphus hypoleucus"
    obtained = summary.build_density_summary(islet, specie)
    obtained_keys = list(obtained.keys())
    expected_keys = [
        "islet",
        "first_season",
        "last_season",
        "figure_path",
        "metodo_busqueda",
        "searching_method",
    ]
    assert obtained_keys == expected_keys
    assert obtained["first_season"] == 2018
    assert obtained["last_season"] == 2022
    assert obtained["islet"] == islet
    assert obtained["figure_path"] == "figures/density_map_gumu_morro_until_filter_season.png"
    assert obtained["metodo_busqueda"] == "muestreo por cuadrantes"
    assert obtained["searching_method"] == "quadrant sampling"

    islet = "Zapato"
    obtained = summary.build_density_summary(islet, specie)
    assert obtained["figure_path"] == "figures/density_map_gumu_zapato_until_filter_season.png"

    exhaustive_burrows_data = pd.read_csv("tests/data/nidos_busqueda_aves_marinas_tests.csv")
    summary = Summary_Constructor(exhaustive_burrows_data)
    islet = "Punta Sur"
    survey_method = "Burrows"
    obtained = summary.build_density_summary(islet, specie, survey_method)
    assert obtained["figure_path"] == "figures/density_map_gumu_punta_sur_until_filter_season.png"
    assert obtained["metodo_busqueda"] == "búsqueda exhaustiva"
    assert obtained["searching_method"] == "exhaustive search"
