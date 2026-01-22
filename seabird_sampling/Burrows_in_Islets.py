from abc import abstractmethod
from geci_plots import fix_date, plot_location_plot
from geoambiental import get_kernel_density
from geoambiental.io import import_coast_line
from .density_maps_tools import (
    filter_dataframe,
    margins_from_polygon,
    initilizate_map_plot,
    generate_PointArray_from_coordinates,
)

import pandas as pd
import numpy as np


class AbstractBurrows:
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    def __init__(self, paths):
        self.input_data_type = paths.input[0][0]
        self._import_coast_line(paths.input[2][0])
        self._load_data(paths.input[1][0])
        self.colonia = paths.input[3][0]
        self.especie = paths.input[4][0]
        self._clean_date(int(paths.input[5][0]))
        self.scale_location = "lower center"
        self.number_of_xticks = 5

    def _load_data(self, burrows_data_path):
        self.burrows_data = pd.read_csv(burrows_data_path)

    def _import_coast_line(self, shapefile_path):
        self.coast_line = import_coast_line(shapefile_path)

    def _clean_date(self, anio):
        self.burrows_data.Fecha = self.burrows_data.Fecha.apply(lambda fecha: fix_date(str(fecha)))
        self.burrows_data.Fecha = pd.to_datetime(self.burrows_data.Fecha)
        if anio != 0:
            if self.especie == "Phoebastria immutabilis":
                years = f"{anio-1}-{anio}"
                self.burrows_data = self.burrows_data[self.burrows_data.Temporada == years]
            else:
                self.burrows_data = self.burrows_data[self.burrows_data.Fecha.dt.year == anio]

    def set_coordinate(self):
        burrows_in_quadrants = filter_dataframe(
            self.burrows_data, self.especie, self.colonia, self.input_data_type
        )
        burrows_in_quadrants.dropna(subset=["Coordenada_Este", "Coordenada_Norte"], inplace=True)
        self.east_coordinates = burrows_in_quadrants.Coordenada_Este
        self.north_coordinates = burrows_in_quadrants.Coordenada_Norte

    def get_coordinates(self):
        return (self.east_coordinates, self.north_coordinates)

    def calculate_kernel(self):
        burrows_points = generate_PointArray_from_coordinates(
            self.east_coordinates, self.north_coordinates
        )
        self.kernel = get_kernel_density(burrows_points, bandwidth=25)

    def normalize_density(self):
        self.normalized_density = np.array(self.kernel[2]) / np.nanmax(self.kernel[2])

    @abstractmethod
    def custom_plot(self):
        pass

    @abstractmethod
    def set_plot_location(self):
        pass


class ConcreteBurrowsFactory:
    def __init__(self, paths):
        self.colonia = paths.input[3][0]
        self.paths = paths

    def create_burrows(self):
        options = {
            "Zapato": ZapatoBurrows(self.paths),
            "Morro Prieto": MorroPrietoBurrows(self.paths),
            "Punta Sur": PuntaSurBurrows(self.paths),
            "Isla principal": PuntaSurBurrows(self.paths),
            "Reserva": ReservaBurrows(self.paths),
        }
        return options[self.colonia]


class ReservaBurrows(AbstractBurrows):
    def custom_plot(self):
        self.costa_islote = self.coast_line
        self.img_x = 220
        self.img_y = 250
        self.bar_width = 50
        self.bar_length = 2000
        self.scale_location = "lower right"
        self.number_of_xticks = 3
        self.fig, self.ax = initilizate_map_plot(self.costa_islote)

    def set_plot_location(self):
        self.margen_x, self.margen_y = margins_from_polygon(
            self.costa_islote, gap_left=1000, gap_right=1000, gap_up=1000, gap_down=1000
        )

    def set_coordinate(self):
        burrows_in_quadrants = self.burrows_data[
            (self.burrows_data.Isla.str.contains("Guadalupe"))
            & (self.burrows_data.Especie == self.especie)
        ].copy()
        burrows_in_quadrants.dropna(subset=["Coordenada_Este", "Coordenada_Norte"], inplace=True)
        self.east_coordinates = burrows_in_quadrants.Coordenada_Este
        self.north_coordinates = burrows_in_quadrants.Coordenada_Norte


class ZapatoBurrows(AbstractBurrows):
    def custom_plot(self):
        self.costa_islote = self.coast_line[12]
        self.img_x = 300
        self.img_y = 350
        self.bar_width = 3
        self.bar_length = 150
        self.fig, self.ax = initilizate_map_plot(self.costa_islote)

    def set_plot_location(self):
        self.margen_x, self.margen_y = margins_from_polygon(
            self.costa_islote, gap_left=400, gap_right=50, gap_up=200, gap_down=200
        )
        plot_location_plot(self.ax, self.coast_line, self.margen_x, self.margen_y, box_length=300)


class MorroPrietoBurrows(AbstractBurrows):
    def custom_plot(self):
        self.costa_islote = self.coast_line[1]
        self.img_x = 220
        self.img_y = 250
        self.bar_width = 3
        self.bar_length = 50
        self.fig, self.ax = initilizate_map_plot(self.costa_islote)

    def set_plot_location(self):
        self.margen_x, self.margen_y = margins_from_polygon(
            self.costa_islote, gap_left=200, gap_right=50, gap_up=50, gap_down=50
        )
        plot_location_plot(self.ax, self.coast_line, self.margen_x, self.margen_y, box_length=500)


class PuntaSurBurrows(AbstractBurrows):
    def custom_plot(self):
        self.costa_islote = self.coast_line
        self.img_x = 2450
        self.img_y = 220
        self.bar_length = 150
        self.bar_width = 10
        self.fig, self.ax = initilizate_map_plot(self.costa_islote)

    def set_plot_location(self):
        self.margen_x = [373400, 375400]
        self.margen_y = [3195200, 3197000]
        plot_location_plot(self.ax, self.coast_line, self.margen_x, self.margen_y, box_length=500)
