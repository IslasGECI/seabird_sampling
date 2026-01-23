from seabird_sampling.Burrows_in_Islets import ConcreteBurrowsFactory
from seabird_sampling.Plotter_Burrows import Plotter_Burrows

import matplotlib.pyplot as plt


class Path:
    def __init__(self, islote, data_type="Quadrants", species="Synthliboramphus hypoleucus"):
        data_path = {
            "Quadrants": "tests/data/madrigueras_cuadrantes_avesmarinas_test.csv",
            "Burrows": "tests/data/nidos_busqueda_aves_marinas_tests.csv",
        }
        self.input = [
            [data_type],
            [data_path[data_type]],
            ["tests/data/linea_costa_isla_guadalupe.shp"],
            [islote],
            [species],
            ["2018"],
            ["tests/data/rosewind.png"],
            ['{"Show Points": "No"}'],
        ]
        self.output = [["tests/data/mapa.png"]]


zapato_paths = Path("Zapato")


def test_create_zapato_burrow():
    Factory = ConcreteBurrowsFactory(zapato_paths)
    Madrigueras = Factory.create_burrows()
    zapato_expected_bar_width = 3
    zapato_expected_bar_length = 150
    Madrigueras.custom_plot()
    assert Madrigueras.bar_length == zapato_expected_bar_length
    assert Madrigueras.bar_width == zapato_expected_bar_width
    assert Madrigueras.scale_location == "lower center"
    zapato_expected_img_x = 300
    zapato_expected_img_y = 350
    assert Madrigueras.img_x == zapato_expected_img_x
    assert Madrigueras.img_y == zapato_expected_img_y


prieto_paths = Path("Morro Prieto")


def test_create_morro_prieto_burrow():
    Factory = ConcreteBurrowsFactory(prieto_paths)
    Madrigueras = Factory.create_burrows()
    Madrigueras.set_coordinate()
    obtained_coordinates = Madrigueras.get_coordinates()
    assert len(obtained_coordinates[0]) == 455
    prieto_expected_bar_width = 3
    prieto_expected_bar_length = 50
    Madrigueras.custom_plot()
    assert Madrigueras.bar_length == prieto_expected_bar_length
    assert Madrigueras.bar_width == prieto_expected_bar_width
    assert Madrigueras.scale_location == "lower center"


prieto_paths_laal = Path("Morro Prieto", "Burrows", "Phoebastria immutabilis")


def test_create_morro_prieto_burrow_for_laal():
    Factory = ConcreteBurrowsFactory(prieto_paths_laal)
    Madrigueras = Factory.create_burrows()
    Madrigueras.set_coordinate()
    obtained_coordinates = Madrigueras.get_coordinates()
    assert len(obtained_coordinates[0]) == 10


punta_paths = Path("Punta Sur")


def test_create_punta_sur_burrow():
    Factory = ConcreteBurrowsFactory(punta_paths)
    Madrigueras = Factory.create_burrows()
    punta_expected_bar_width = 10
    punta_expected_bar_length = 150
    Madrigueras.custom_plot()
    assert Madrigueras.bar_length == punta_expected_bar_length
    assert Madrigueras.bar_width == punta_expected_bar_width
    assert Madrigueras.scale_location == "lower center"


isla_principal_paths_gumu = Path("Isla principal", "Burrows")


def test_create_isla_principal_burrow():
    Factory = ConcreteBurrowsFactory(isla_principal_paths_gumu)
    Madrigueras = Factory.create_burrows()
    Madrigueras.set_coordinate()
    obtained_coordinates = Madrigueras.get_coordinates()
    assert len(obtained_coordinates[0]) == 8
    assert Madrigueras.scale_location == "lower center"


all_reserve = Path("Reserva", "Burrows", "Phoebastria immutabilis")


def test_create_reserva_burrows():
    Factory = ConcreteBurrowsFactory(all_reserve)
    Madrigueras = Factory.create_burrows()
    Madrigueras.set_coordinate()
    obtained_coordinates = Madrigueras.get_coordinates()
    expected_number_of_points = 11
    assert len(obtained_coordinates[0]) == expected_number_of_points

    Madrigueras.custom_plot()
    reserva_expected_bar_width = 50
    reserva_expected_bar_length = 2000
    assert Madrigueras.bar_length == reserva_expected_bar_length
    assert Madrigueras.bar_width == reserva_expected_bar_width
    Madrigueras.set_plot_location()
    gap = 1000
    expected_margen_x_min = 367200 - gap
    assert Madrigueras.margen_x[0] == expected_margen_x_min
    expected_margen_x_max = 381000 + gap
    assert Madrigueras.margen_x[1] == expected_margen_x_max
    expected_margen_y_min = 3191800 - gap
    assert Madrigueras.margen_y[0] == expected_margen_y_min
    expected_margen_y_max = 3229700 + gap
    assert Madrigueras.margen_y[1] == expected_margen_y_max
    assert Madrigueras.scale_location == "lower right"
    assert Madrigueras.number_of_xticks == 3


def tests_Plotter_Burrows():
    Factory = ConcreteBurrowsFactory(zapato_paths)
    Madrigueras = Factory.create_burrows()
    Madrigueras.set_coordinate()
    Madrigueras.calculate_kernel()
    Madrigueras.normalize_density()
    Madrigueras.custom_plot()
    Plotter = Plotter_Burrows(zapato_paths)
    assert Plotter.rose_wind.size == (98, 200)
    Madrigueras.set_plot_location()
    Plotter.plot_coast(Madrigueras)
    Plotter.pimp_plot(Madrigueras)
    Plotter.save_plot()
    obtained_axis = plt.gca()
    assert len(obtained_axis.get_xticklabels()) == 5
    expected_margen_x_min = 374100
    assert Madrigueras.margen_x[0] == expected_margen_x_min
    expected_margen_x_max = 375400
    assert Madrigueras.margen_x[1] == expected_margen_x_max
    expected_margen_y_min = 3191600
    assert Madrigueras.margen_y[0] == expected_margen_y_min
    expected_margen_y_max = 3192700
    assert Madrigueras.margen_y[1] == expected_margen_y_max

    Factory = ConcreteBurrowsFactory(all_reserve)
    Madrigueras = Factory.create_burrows()
    Madrigueras.custom_plot()
    Madrigueras.set_plot_location()
    Plotter = Plotter_Burrows(all_reserve)
    Plotter.pimp_plot(Madrigueras)
    obtained_axis = plt.gca()
    expected_number_of_xticks = 3
    assert len(obtained_axis.get_xticklabels()) == expected_number_of_xticks
    expected_horizontal_alignment = "center"
    obtained_horizontal_alignment = (
        obtained_axis.get_xaxis().get_ticklabels()[0].get_horizontalalignment()
    )
    assert obtained_horizontal_alignment == expected_horizontal_alignment
    expected_vertical_alignment = "center_baseline"
    obtained_vertical_alignment = (
        obtained_axis.get_yaxis().get_ticklabels()[0].get_verticalalignment()
    )
    assert obtained_vertical_alignment == expected_vertical_alignment
