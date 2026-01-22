from muestreo_aves_marinas_ipbc.density_maps_tools import initilizate_map_plot
from geoambiental.io import import_coast_line


def test_initialize_density_map():
    coast_line = import_coast_line("tests/data/linea_costa_isla_guadalupe.shp")
    obtained_fig, obtained_ax = initilizate_map_plot(coast_line)
    assert obtained_ax.get_aspect() == 1
