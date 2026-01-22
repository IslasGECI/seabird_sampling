from fastkml import kml
import numpy as np


def read_kml_features(kml_file):
    with open(kml_file, "rt", encoding="utf-8") as myfile:
        doc = myfile.read()

    kml_object = kml.KML()
    kml_data = kml_object.from_string(doc)

    features = list(kml_data.features)
    kml_features = list(features[0].features)
    return kml_features


def get_latitude_from_kml(kml_features):
    numpy_coordinates = np.array(kml_features[0].geometry.exterior.coords)
    latitudes = numpy_coordinates[:, 1]
    return latitudes


def get_longitude_from_kml(kml_features):
    numpy_coordinates = np.array(kml_features[0].geometry.exterior.coords)
    longitudes = numpy_coordinates[:, 0]
    return longitudes
