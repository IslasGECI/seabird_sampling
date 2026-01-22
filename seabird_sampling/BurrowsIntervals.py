from .plot_error_bar import make_sure_folder_exists
from .process_data import join_exhaustive_and_sampling

import json
import numpy as np


class BurrowSeries:
    def __init__(self, exhaustive_data, central_and_deltas_densities, kernel_area):
        self.exhaustive = exhaustive_data
        self.central_and_deltas_densities = central_and_deltas_densities
        self._burrow_series_with_deltas(kernel_area)
        self._set_seasons()
        self.correction_factor = self._calculate_correction_factor()
        self._set_serie_of_central_values()

    def _set_nidos_2018(self):
        year_with_exhaustive_and_sampling_searches = 2018
        self.nidos_2018 = self.exhaustive[
            self.exhaustive.Temporada == year_with_exhaustive_and_sampling_searches
        ].Total_nidos.iloc[0]

    def _set_seasons(self):
        exhaustive_seasons = np.array(self.exhaustive["Temporada"], dtype=str)
        sampling_seasons = np.array(self.central_and_deltas_densities.temporada, dtype=str)
        self.seasons = np.unique(np.append(exhaustive_seasons, sampling_seasons))

    def _burrow_series_with_deltas(self, kernel_area):
        self.burrows_central_and_deltas = self.central_and_deltas_densities
        self.burrows_central_and_deltas.loc[:, ["central", "minimo", "maximo"]] = (
            self.burrows_central_and_deltas.loc[:, ["central", "minimo", "maximo"]]
            * kernel_area["area"]
        )

    def _calculate_correction_factor(self):
        correction_factor = 1
        if self._is_sampling_in_2018():
            self._set_nidos_2018()
            correction_factor = (
                self.burrows_central_and_deltas[
                    self.burrows_central_and_deltas.temporada == 2018
                ].central.iloc[0]
                / self.nidos_2018
            )
        return np.max([correction_factor, 1])

    def get_error_deltas(self):
        return self.burrows_central_and_deltas.loc[:, ["temporada", "minimo", "maximo"]]

    def _set_serie_of_central_values(self):
        exhaustive_corrected = self.exhaustive.copy()
        exhaustive_corrected.Total_nidos = self.exhaustive.Total_nidos * self.correction_factor
        self.serie_of_central_values = join_exhaustive_and_sampling(
            exhaustive_corrected, self.burrows_central_and_deltas
        )

    def get_table_of_central_values(self):
        renamed_df = self.serie_of_central_values.rename(
            columns={"Total_nidos": "Cantidad de nidos"}
        )
        return renamed_df.loc[:, ["Temporada", "Cantidad de nidos"]]

    def _is_sampling_in_2018(self):
        return 2018 in self.burrows_central_and_deltas.temporada.values


def write_error_bars_json(barras_error_df, ruta_intervalo_error):
    make_sure_folder_exists("reports/non-tabular")
    with open(ruta_intervalo_error, "w") as exit_file:
        json.dump(
            {
                "temporada": barras_error_df["temporada"].tolist(),
                "minimo": barras_error_df["minimo"].tolist(),
                "maximo": barras_error_df["maximo"].tolist(),
            },
            exit_file,
        )
