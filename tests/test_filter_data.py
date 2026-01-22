from muestreo_aves_marinas_ipbc import (
    count_burrows,
    count_total_burrows_per_season,
    filter_per_specie_and_colony,
)

import pandas as pd


burrows_data = pd.DataFrame(
    {
        "Sitio_o_colonia": [
            "Morro Prieto",
            "Isla Principal - Dentro cerco",
            "Isla Principal - Fuera cerco",
            "Isla Principal - Dentro cerco",
            "Roca Muela",
        ],
        "Especie": ["gumu", "shearwater", "tosh", "tosh", "tosh"],
        "ID_madriguera": ["GM3006", "GM3007", "GM3008", "GM3009", "GM3010"],
        "Temporada": ["2017", "2017", "2017", "2018", 2018],
    }
)


def test_filter_per_specie_and_colony():
    especie = "gumu"
    colonia = "Morro Prieto"
    obtained = filter_per_specie_and_colony(burrows_data, especie, colonia)
    expected_rows = 1
    obtained_rows = len(obtained)
    assert obtained_rows == expected_rows

    especie = "tosh"
    colonia = "Isla Principal|Roca"
    obtained = filter_per_specie_and_colony(burrows_data, especie, colonia)
    expected_rows = 3
    obtained_rows = len(obtained)
    assert obtained_rows == expected_rows


def test_count_burrows():
    obtained = count_burrows(burrows_data)
    expected_index = "Temporada"
    assert obtained.index.name == expected_index
    expected_columns = ["Total_nidos"]
    assert list(obtained.columns) == expected_columns
    expected_rows = 2
    obtained_rows = len(obtained)
    assert obtained_rows == expected_rows

    burrows_data_with_two_years_nesting_season = pd.DataFrame(
        {
            "Sitio_o_colonia": [
                "Morro Prieto",
                "Isla Principal - Dentro cerco",
                "Isla Principal - Fuera cerco",
                "Isla Principal - Dentro cerco",
                "Roca Muela",
            ],
            "Especie": ["laal", "shearwater", "tosh", "tosh", "tosh"],
            "ID_madriguera": ["GM3006", "GM3007", "GM3008", "GM3009", "GM3010"],
            "Temporada": ["2017-2018", "2017", "2017", "2018", 2018],
        }
    )
    obtained = count_burrows(burrows_data_with_two_years_nesting_season)

    expected_rows = 2
    obtained_rows = len(obtained)
    assert obtained_rows == expected_rows


def test_count_total_burrows_per_season():
    especie = "tosh"
    colonia = "Isla Principal"
    obtained = count_total_burrows_per_season(burrows_data, especie, colonia)
    expected_season = ["2017", "2018"]
    expected_counts = [1, 1]
    assert list(obtained.index) == expected_season
    assert (obtained.Total_nidos == expected_counts).all()
