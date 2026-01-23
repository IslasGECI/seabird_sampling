from seabird_sampling.calculate_nesting_zone_from_kml import (
    get_latitude_from_kml,
    get_longitude_from_kml,
    read_kml_features,
)

import numpy as np
from pytest import approx


kml_file = "tests/data/area_colonia_mergulo_zapato.kml"
kml_features = read_kml_features(kml_file)


def test_read_kml_features():
    obtained = read_kml_features(kml_file)
    assert type(obtained) is list


def test_get_latitude_from_kml():
    obtained_latitudes = get_latitude_from_kml(kml_features)
    assert type(obtained_latitudes) is np.ndarray

    expected_first_latitude = 28.84814225094694
    obtained_first_latitude = obtained_latitudes[0]
    assert obtained_first_latitude == approx(expected_first_latitude)


def test_get_longitude_from_kml():
    obtained_longitudes = get_longitude_from_kml(kml_features)
    expected_first_longitude = -118.283147223648
    obtained_first_longitude = obtained_longitudes[0]
    assert obtained_first_longitude == approx(expected_first_longitude)
