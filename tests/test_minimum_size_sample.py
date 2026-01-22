from muestreo_aves_marinas_ipbc.minimum_size_sample import (
    calculate_variation_coefficient,
    calculate_sample_size_for_an_error_of,
)
import pandas as pd
import pytest

madrigueras = pd.read_csv("tests/data/madrigueras_cuadrantes_avesmarinas_test.csv")
madrigueras["year"] = madrigueras.Fecha.str.slice(7, 12).astype(int)
madrigueras_gumu_2014_morro_prieto = madrigueras[
    (madrigueras.Especie == "Synthliboramphus hypoleucus")
    & (madrigueras.Sitio_o_colonia == "Morro Prieto")
    & (madrigueras.year == 2018)
]

print(madrigueras_gumu_2014_morro_prieto)

madrigueras_bvsh_2024_zapato = madrigueras[
    (madrigueras.Especie == "Puffinus opisthomelas")
    & (madrigueras.Sitio_o_colonia == "Zapato")
    & (madrigueras.year == 2024)
]


def tests_calculate_sample_size_for_an_error_of():
    percentage_error = 10
    obtained = calculate_sample_size_for_an_error_of(
        madrigueras_gumu_2014_morro_prieto, percentage_error
    )
    assert isinstance(obtained, int)
    obtained = calculate_sample_size_for_an_error_of(madrigueras_bvsh_2024_zapato, percentage_error)
    assert pytest.approx(obtained, rel=1e-1) == 625

    percentage_error_df = pd.DataFrame(
        {
            "percentage_error": [40, 30, 20, 10, 5],
        }
    )
    percentage_error_df["sample_size"] = calculate_sample_size_for_an_error_of(
        madrigueras_bvsh_2024_zapato, percentage_error_df.percentage_error
    )
    obtained_sample_size = percentage_error_df.sample_size.to_list()
    expected_sample_size = [39, 69, 156, 625, 2499]

    assert obtained_sample_size == expected_sample_size


def tests_minimum_size():
    obtained = calculate_variation_coefficient(madrigueras_gumu_2014_morro_prieto)
    assert isinstance(obtained, float)
    assert obtained < 0.75

    with pytest.raises(
        ValueError,
        match="Coeficiente de variación muy alto. Necesitamos tamaño de la muestra > 220",
    ):
        calculate_variation_coefficient(madrigueras_bvsh_2024_zapato)
