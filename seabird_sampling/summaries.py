from .filter_data import filter_per_specie_and_colony
from geci_plots import fix_date

import pandas as pd


class Summary_Constructor:
    def __init__(self, burrows_data):
        self.burrows_data = self._clean_date(burrows_data)

    def build_density_summary(self, islet, species, survey_method="Quadrants"):
        filtered_burrows_data = filter_per_specie_and_colony(self.burrows_data, species, islet)
        years = filtered_burrows_data.Fecha.dt.year
        return {
            "islet": islet,
            "first_season": years.min(),
            "last_season": years.max(),
            "figure_path": self._figure_path_dictionary(islet, species),
            "metodo_busqueda": self._survey_method_dictionary(survey_method)["es"],
            "searching_method": self._survey_method_dictionary(survey_method)["en"],
        }

    def _figure_path_dictionary(self, islet, species):
        density_figure_dictionary = {
            "Morro Prieto": {
                "Synthliboramphus hypoleucus": "figures/density_map_gumu_morro_until_filter_season.png"
            },
            "Punta Sur": {
                "Synthliboramphus hypoleucus": "figures/density_map_gumu_punta_sur_until_filter_season.png"
            },
            "Zapato": {
                "Synthliboramphus hypoleucus": "figures/density_map_gumu_zapato_until_filter_season.png"
            },
        }
        return density_figure_dictionary[islet][species]

    def _survey_method_dictionary(self, survey_method):
        survey_method_dictionary = {
            "Quadrants": {"es": "muestreo por cuadrantes", "en": "quadrant sampling"},
            "Burrows": {"es": "búsqueda exhaustiva", "en": "exhaustive search"},
        }
        return survey_method_dictionary[survey_method]

    def _clean_date(self, raw_burrows_data):
        raw_burrows_data.Fecha = raw_burrows_data.Fecha.apply(lambda fecha: fix_date(fecha))
        raw_burrows_data.Fecha = pd.to_datetime(raw_burrows_data.Fecha)
        return raw_burrows_data
