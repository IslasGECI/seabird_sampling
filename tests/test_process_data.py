from seabird_sampling.process_data import (
    join_exhaustive_and_sampling,
)

import pandas as pd


def test_join_exhaustive_and_sampling():
    data_exhaustive = pd.DataFrame({"Temporada": ["2017", "2018"], "Total_nidos": [10, 20]})
    expected_2018_value = 330
    datos_madrigueras_kernel = pd.DataFrame(
        {"temporada": ["2018", "2022", "2023"], "central": [expected_2018_value, 554.58, 422.08]}
    )
    obtained = join_exhaustive_and_sampling(data_exhaustive, datos_madrigueras_kernel)

    obtained_length = len(obtained)
    expected_length = 4
    assert obtained_length == expected_length

    obtained_2018_value = obtained.Total_nidos.iloc[1]
    assert expected_2018_value == obtained_2018_value

    obtained_shape = obtained.shape
    expected_shape = (expected_length, 2)
    assert obtained_shape == expected_shape

    datos_madrigueras_kernel = pd.DataFrame(
        {"temporada": ["2021", "2022", "2023"], "central": [330, 554.58, 422.08]}
    )
    obtained = join_exhaustive_and_sampling(data_exhaustive, datos_madrigueras_kernel)

    obtained_length = len(obtained)
    expected_length = 5
    assert obtained_length == expected_length

    expected_exhaustive_2021 = 1.0
    data_exhaustive = pd.DataFrame(
        {
            "Temporada": ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
            "Total_nidos": [1753.0, 1039.0, 570.0, 907.0, 761.0, expected_exhaustive_2021, 1141.0],
        }
    )
    datos_madrigueras_kernel = pd.DataFrame(
        {"temporada": ["2018", "2019", "2020", "2022"], "central": [563.8, 896.1, 757.2, 1130.9]}
    )
    obtained = join_exhaustive_and_sampling(data_exhaustive, datos_madrigueras_kernel)
    assert obtained.Total_nidos.iloc[5] == expected_exhaustive_2021
