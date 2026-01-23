import pytest
from seabird_sampling.plot_burrows_density_map import set_plot, choose_coast_line
import numpy as np


@pytest.mark.mpl_image_compare(tolerance=0)
def test_set_plot():
    figure = set_plot()
    return figure


def test_choose_coast_line():
    islet = "Morro Prieto"
    linea_costa = np.arange(0, 15, 1)

    expected_linea_costa_islote = linea_costa[1]
    expected_margen_superior_isla = 70

    obtained_linea_costa_islote, obtained_margen_superior_isla = choose_coast_line(
        islet, linea_costa
    )

    assert (
        expected_linea_costa_islote == obtained_linea_costa_islote
    ), "CASE 1 - MORRO PRIETO linea costa"
    assert (
        expected_margen_superior_isla == obtained_margen_superior_isla
    ), "CASE 1 - MORRO PRIETO margen superior"

    # CASE 2 - ZAPATO
    islet = "Zapato"

    expected_linea_costa_islote = linea_costa[12]
    expected_margen_superior_isla = 100

    obtained_linea_costa_islote, obtained_margen_superior_isla = choose_coast_line(
        islet, linea_costa
    )

    assert expected_linea_costa_islote == obtained_linea_costa_islote
    assert expected_margen_superior_isla == obtained_margen_superior_isla
