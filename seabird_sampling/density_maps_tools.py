from distdens.models import SamplingQuadrat
from geci_plots import roundup
from geoambiental import Map, PointArray
import matplotlib as mpl
from matplotlib.colors import ListedColormap
from scipy.interpolate import griddata

from .filter_data import filter_per_specie_and_colony

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import utm

land_color = "#FFFAE6"
sea_color = "#E6FFFF"


def coordinates_from_quadrants(quadrants_array):
    north_coordinate = np.array([quadrant.y for quadrant in quadrants_array])
    east_coordinate = np.array([quadrant.x for quadrant in quadrants_array])
    return north_coordinate, east_coordinate


def concatenate_quadrants_with_coast_line(quadrants_array, geoambiental_polygon, UTM_zone="11R"):
    quadrants = np.copy(quadrants_array)
    for x, y in zip(geoambiental_polygon.x, geoambiental_polygon.y):
        lat, lon = utm.to_latlon(x, y, int(UTM_zone[0:2]), UTM_zone[-1])
        quadrants = np.concatenate([quadrants, np.array([SamplingQuadrat(lat, lon, 1, 0)])])
    return quadrants


def set_density_colorbar(density_array, contour_plot, label_size=20):
    density = np.nan_to_num(density_array)
    ticks_postitions = [np.min(density), np.max(density)]
    cbar = plt.colorbar(contour_plot, ticks=ticks_postitions)
    cbar.ax.set_yticklabels(["Low", "High"], size=label_size)
    cbar.solids.set_rasterized(True)
    cbar.solids.set_edgecolor("face")
    cbar.set_label("Burrow density", size=label_size)


def adjust_colormap():
    hot = mpl.colormaps["hot_r"].resampled(256)
    newcolors = hot(np.linspace(0, 1, 256))
    newcolors[:8, 2] = 0.8984375
    newcolors[:68, 1] = 0.9765625
    newcolors[:164, 0] = 0.99609375
    return ListedColormap(newcolors)


def initilizate_map_plot(geoambiental_polygon, fig_size=(15.3, 10.4)):
    fig, ax = plt.subplots(figsize=fig_size)
    plt.yticks(rotation=90)
    plt.gca().ticklabel_format(useOffset=False)
    plt.gca().set_facecolor(sea_color)
    plt.fill(
        geoambiental_polygon.x,
        geoambiental_polygon.y,
        facecolor=land_color,
        edgecolor="black",
        linewidth=1,
        zorder=0,
    )
    ax.set_aspect("equal")
    return fig, ax


def margins_from_coordinate(polygon_coordinates, gap_min=100, gap_max=100, n_points=100):
    margin = [
        roundup(min(polygon_coordinates) - gap_min, n_points),
        roundup(max(polygon_coordinates) + gap_max, n_points),
    ]
    return margin


def margins_from_polygon(
    geoambiental_polygon, gap_left=100, gap_right=100, gap_up=100, gap_down=100, n_points=100
):
    margin_x = margins_from_coordinate(geoambiental_polygon.x, gap_left, gap_right, n_points)
    margin_y = margins_from_coordinate(geoambiental_polygon.y, gap_down, gap_up, n_points)
    return margin_x, margin_y


def generate_grid_from_limits(east_coordinate, north_coordinate, n_dim=100):
    grid_x, grid_y = np.meshgrid(
        np.linspace(min(east_coordinate), max(east_coordinate), n_dim),
        np.linspace(min(north_coordinate), max(north_coordinate), n_dim),
    )
    return grid_x, grid_y


def get_density_from_quadrants(quadrants_array):
    return np.array([quadrant.get_density() for quadrant in quadrants_array])


def calculate_grid_arrays_from_quadrants(quadrants_array):
    density = get_density_from_quadrants(quadrants_array)
    north_coordinate, east_coordinate = coordinates_from_quadrants(quadrants_array)
    grid_x, grid_y = generate_grid_from_limits(east_coordinate, north_coordinate)
    grid_z = griddata(
        np.column_stack([east_coordinate, north_coordinate]), density, (grid_x, grid_y), "cubic"
    )
    grid_z[grid_z <= 0] = np.nan
    return grid_x, grid_y, grid_z


def generate_density_map_from_quadrants(quadrants_array):
    grid_x, grid_y, grid_z0 = calculate_grid_arrays_from_quadrants(quadrants_array)
    return Map(grid_y[:, 0], grid_x[0, :], grid_z0)


def generate_PointArray_from_coordinates(east_coordinate, north_coordinate):
    latitude = []
    longitude = []
    for east, north in zip(east_coordinate, north_coordinate):
        lat, lon = utm.to_latlon(east, north, 11, "R")
        latitude.append(lat)
        longitude.append(lon)
    return PointArray(latitude, longitude)


def quadrants_to_burrows(dataframe):
    east = []
    north = []
    for _, row in dataframe.iterrows():
        for j in range(int(row.Total_de_madrigueras)):
            east.append(row.Coordenada_Este)
            north.append(row.Coordenada_Norte)
    return pd.DataFrame({"Coordenada_Este": east, "Coordenada_Norte": north})


def filter_dataframe(burrows_data, especie, colonia, input_data_type):
    if input_data_type == "Quadrants":
        burrows_in_quadrants = filter_per_specie_and_colony(burrows_data, especie, colonia)
        burrows_in_quadrants = burrows_in_quadrants.dropna(subset=["Total_de_madrigueras"])
        burrows_in_quadrants = quadrants_to_burrows(burrows_in_quadrants)
    elif input_data_type == "Burrows":
        if (especie == "Phoebastria immutabilis") and (colonia == "Punta Sur"):
            albatros_data = burrows_data[burrows_data.Especie == especie]
            remove_list = ["Morro Prieto", "Zapato"]
            burrows_in_quadrants = albatros_data[
                ~albatros_data["Sitio_o_colonia"].isin(remove_list)
            ]
        else:
            burrows_in_quadrants = filter_per_specie_and_colony(burrows_data, especie, colonia)
    return burrows_in_quadrants
