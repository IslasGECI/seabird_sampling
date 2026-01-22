import numpy as np
import pandas as pd


def combine_error_bars(error_morro, error_zapato):
    barras_error_morro = pd.DataFrame(error_morro).set_index("temporada")
    barras_error_zapato = pd.DataFrame(error_zapato).set_index("temporada")

    barras_error = barras_error_morro.add(barras_error_zapato, fill_value=0)
    return barras_error.reset_index().rename(columns={"index": "temporada"})


def max_min_from_dataframe(dataframe):
    return np.array([dataframe["minimo"], dataframe["maximo"]])
