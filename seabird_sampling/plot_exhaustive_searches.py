from geci_plots import (
    geci_plot,
    plt,
    rounded_ticks_array,
)
import numpy as np


def plot_exhaustive_searches(exhaustive_data, output_path):
    temporadas = np.array(exhaustive_data.Temporada, dtype=str)
    total_nidos = np.array(exhaustive_data.Total_nidos)
    number_of_seasons = len(temporadas)
    posiciones = np.linspace(1, number_of_seasons, number_of_seasons)

    fig, ax = geci_plot()
    ax.set_xlabel("Breeding season", fontsize=25, labelpad=10)
    ax.set_ylabel("Total of breeding pairs", fontsize=25, labelpad=10)
    ax.tick_params(labelsize=13)
    ax.plot(posiciones, total_nidos, "-Db", markerfacecolor="blue")
    limite_superior = np.max(total_nidos) * 1.05
    ax.set_ylim(0, limite_superior)

    extra_tick_index = len(temporadas) - 1
    posiciones[extra_tick_index] = posiciones[extra_tick_index] + 0.05
    plt.xlim(0, posiciones[-1])

    plt.xticks(posiciones, temporadas)
    y_ticks_array = rounded_ticks_array(limite_superior, 0)
    plt.yticks(y_ticks_array)
    plt.tick_params(labelsize=20)
    plt.savefig(output_path, dpi=300)
