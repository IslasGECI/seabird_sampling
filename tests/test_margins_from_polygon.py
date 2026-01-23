from geoambiental.io import import_coast_line
from seabird_sampling.density_maps_tools import margins_from_polygon

import numpy as np


def test_margins_from_polygon():
    costa_islote = import_coast_line("tests/data/linea_costa_isla_guadalupe.shp")
    obtained_margin_x, obtained_margin_y = margins_from_polygon(costa_islote)
    assert np.shape(obtained_margin_x) == (2,)
    assert np.shape(obtained_margin_y) == (2,)
    assert not np.isnan(obtained_margin_x).any()
    assert not np.isnan(obtained_margin_y).any()
