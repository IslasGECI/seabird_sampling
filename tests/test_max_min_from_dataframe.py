import pandas as pd
import numpy as np
from seabird_sampling.max_min_from_dataframe import (
    max_min_from_dataframe,
    combine_error_bars,
)


def test_combine_error_bars():
    errors_1 = {
        "temporada": [2001, 2002, 2003, 2004],
        "minimo": [1, 2, 3, 4],
        "maximo": [5, 6, 7, 8],
    }
    errors_2 = {
        "temporada": [2001, 2002, 2003, 2004],
        "minimo": [10, 20, 30, 40],
        "maximo": [50, 60, 70, 80],
    }
    obtained = combine_error_bars(errors_1, errors_2)
    expected = pd.DataFrame(
        {
            "temporada": [2001, 2002, 2003, 2004],
            "minimo": [11, 22, 33, 44],
            "maximo": [55, 66, 77, 88],
        }
    )
    pd.testing.assert_frame_equal(obtained, expected)


def test_max_min_from_dataframe():
    datos = pd.DataFrame(
        {"temporada": [2014, 2016], "minimo": [1, 2], "central": [2, 2], "maximo": [3, 4]}
    )
    datos_salida = np.array([datos["minimo"], datos["maximo"]])
    obtained = max_min_from_dataframe(datos)
    np.testing.assert_array_equal(obtained, datos_salida)
