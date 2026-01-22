import pandas as pd


def join_exhaustive_and_sampling(data_exhaustive, data_sampling):
    data_sampling = data_sampling.rename(
        columns={"temporada": "Temporada", "central": "Total_nidos"}
    )
    joined_dataframe = (
        pd.concat([data_exhaustive, data_sampling], ignore_index=True)
        .drop_duplicates(subset=["Temporada"], keep="last")
        .sort_values(by=["Temporada"])
    )
    return joined_dataframe


def is_sampling_in_2018(sampling_data):
    return 2018 in sampling_data.temporada.values


def calculate_correction_factor(sampling_data, nidos_2018):
    correction_factor = 1
    if is_sampling_in_2018(sampling_data):
        correction_factor = (
            sampling_data[sampling_data.temporada == 2018].central.iloc[0] / nidos_2018
        )
    return correction_factor
