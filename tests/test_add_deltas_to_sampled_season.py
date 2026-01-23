from seabird_sampling.add_deltas_to_sampled_season import (
    add_intervals_to_sampled_season,
    add_percentage_error,
    calculate_percentage_error,
    get_intervals_from_error_bars_and_series,
    join_exhaustive_and_sampling_with_intervals,
)

import pandas as pd


error_bars_seasons = [2018, 2019, 2020, 2022]
barras_error_df = pd.DataFrame(
    {
        "temporada": error_bars_seasons,
        "minimo": [
            140.0,
            440.0,
            200.0,
            420.0,
        ],
        "maximo": [170.0, 550.0, 220.0, 540.0],
    }
)


def test_add_intervals_to_sampled_season():
    results_df = pd.DataFrame(
        {
            "Temporada": ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"],
            "Cantidad de nidos": [
                991.0,
                1470.0,
                2050.0,
                2460.0,
                4077.0,
                4125.0,
                3095.0,
                485.02452872676,
            ],
        }
    )
    obtained = add_intervals_to_sampled_season(barras_error_df, results_df)
    assert str(obtained["Cantidad de nidos"][0]) == "991"
    assert str(obtained["Cantidad de nidos"][4]) == "4080 (3640 - 4630)"
    assert str(obtained["Cantidad de nidos"][6]) == "3095"
    assert str(obtained["Cantidad de nidos"][7]) == "490 (70 - 1030)"
    assert obtained.shape[1] == 3


def test_add_percentage_error():
    joined_exhaustive_and_sampling = pd.DataFrame(
        {
            "Temporada": [2016, 2017, 2018, 2019],
            "Cantidad de nidos": [1, 2, "2460 (2320 - 2630)", "4080 (3640 - 4630)"],
        }
    )
    errors_and_central_df = pd.DataFrame(
        {
            "temporada": [2018, 2019],
            "central": [2460, 4080],
            "minimo": [140, 440],
            "maximo": [170, 550],
            "Cantidad de nidos": [2460, 4080],
        }
    )
    obtained = add_percentage_error(joined_exhaustive_and_sampling, errors_and_central_df)
    assert obtained.shape == (4, 3)
    assert obtained.iloc[0, 2] == "-"
    assert isinstance(obtained.iloc[3, 2], int)


def test_join_exhaustive_and_sampling_with_intervals():
    results_df = pd.DataFrame(
        {"Temporada": [2018, 2019, 2020, 2021, 2022], "Cantidad de nidos": [1, 2, 3, 4, 5]}
    )
    errors_and_central = pd.DataFrame(
        {
            "temporada": [2019, 2020, 2022],
            "Cantidad de nidos": ["2.2 (1.1 - 3.3)", "3.3 (2.2 - 4.4)", "5.5 (4.4 - 6.6)"],
            "central": [2, 3, 4],
            "minimo": [1, 2, 3],
            "maximo": [3, 4, 5],
        }
    )
    obtained = join_exhaustive_and_sampling_with_intervals(results_df, errors_and_central)

    assert obtained.shape == (5, 2)


def test_calculate_percentage_error():
    errors_and_central_df = pd.DataFrame(
        {
            "temporada": [2018, 2019, 2020, 2021],
            "central": [2460, 4080, 4120, 490],
            "minimo": [140, 440, 200, 420],
            "maximo": [170, 550, 220, 540],
        }
    )
    obtained = calculate_percentage_error(errors_and_central_df)
    expected_percentage_error = [6, 12, 5, 98]
    obtained_percentage_error_list = obtained.percentage_error.tolist()
    assert obtained_percentage_error_list == expected_percentage_error
    assert obtained.temporada[0] == 2018


def test_get_intervals_from_error_bars_and_series():
    results_dic = pd.DataFrame(
        {
            "Temporada": [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
            "Cantidad de nidos": [
                991.0,
                1470.0,
                2050.0,
                2460.0,
                4077.0,
                4125.0,
                3095.0,
                4536.0,
                5000.0,
            ],
        }
    )
    obtained = get_intervals_from_error_bars_and_series(barras_error_df, results_dic)
    assert obtained.shape == (4, 4)
    assert obtained.temporada.tolist() == error_bars_seasons

    expected_central_values = [4077.0, 4125.0, 3095.0, 5000.0]
    assert obtained.central.tolist() == expected_central_values
