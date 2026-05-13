from seabird_sampling.max_min_from_dataframe import max_min_from_dataframe

from geci_plots import (
    geci_plot,
    plt,
    rounded_ticks_array,
)

import os
import numpy as np


def plot_breeding_pairs_with_error_bars(
    ruta_grafica, datos_madrigueras_kernel, temporadas, serie_kernel
):
    _, ax = geci_plot()
    data_length = len(temporadas)
    posiciones = np.linspace(1, data_length, data_length)
    number_of_seasons_with_sampling = len(datos_madrigueras_kernel)
    plot_error_bars(ax, posiciones[-number_of_seasons_with_sampling:], datos_madrigueras_kernel)
    add_labels(ax)
    ax.plot(posiciones, serie_kernel, "-Db", markerfacecolor="blue")

    add_xticks(plt, temporadas)

    add_yticks(plt, datos_madrigueras_kernel, serie_kernel, ax)

    plt.savefig(ruta_grafica, dpi=300)
    return ax


def add_yticks(plt, datos_madrigueras_kernel, serie_kernel, ax):
    limite_superior = get_superior_limit(datos_madrigueras_kernel, serie_kernel)
    y_ticks_array = rounded_ticks_array(limite_superior, 0)
    plt.yticks(y_ticks_array)
    plt.tick_params(labelsize=20)


def add_yticks_2(ax):
    ax.set_ylim(0, 6000)
    plt.yticks(
        np.arange(
            0,
            6001,
            1000,
        )
    )
    plt.tick_params(labelsize=20)


def add_xticks(plt, temporadas):
    data_length = len(temporadas)
    posiciones = np.linspace(1, data_length, data_length)
    extra_tick_index = data_length - 1
    posiciones[extra_tick_index] = posiciones[extra_tick_index] + 0.05
    plt.xticks(posiciones, temporadas)
    plt.xlim(0, posiciones[-1])


def add_labels(ax):
    ax.set_xlabel("Breeding season", fontsize=25, labelpad=10)
    ax.set_ylabel("Total of breeding pairs", fontsize=25, labelpad=10)
    ax.tick_params(labelsize=13)


def get_superior_limit(df, time_series):
    if np.max(df["central"] + df["maximo"]) >= np.max(time_series):
        superior_limit = np.max(df["central"] + df["maximo"])
    elif np.max(df["central"] + df["maximo"]) < np.max(time_series):
        superior_limit = np.max(time_series)
    return superior_limit


def get_table_salida(temporadas, serie_kernel):
    return {"Temporada": list(temporadas), "Cantidad de nidos": list(serie_kernel)}


def make_sure_folder_exists(folder: str):
    folder_is_missing = not os.path.exists(folder)
    if folder_is_missing:
        os.makedirs(folder)


def plot_error_bars(ax, x, y):
    y_err = max_min_from_dataframe(y)
    ax.errorbar(x, y["central"], yerr=y_err, marker="o", linestyle="None", color="b")
