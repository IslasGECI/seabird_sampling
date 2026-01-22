from geci_plots import plt, set_scale_bar
from .density_maps_tools import adjust_colormap, set_density_colorbar, sea_color
from distdens import fillout

from PIL import Image
import json
import numpy as np


class Plotter_Burrows:
    def __init__(self, paths, plot_density=True):
        self._open_rose_wind(paths.input[6][0])
        self.explicit_points_dictionary = json.loads(paths.input[7][0])
        self.mapa_densidad_ruta = paths.output[0][0]
        self.plot_density = plot_density

    def _open_rose_wind(self, path_rose_wind):
        opened_wind_rose = Image.open(path_rose_wind)
        new_size = (opened_wind_rose.width // 2, opened_wind_rose.height // 2)
        self.rose_wind = opened_wind_rose.resize(new_size, Image.Resampling.LANCZOS)

    def _calculate_countourn_plot(self, Burrows):
        new_hot_r = adjust_colormap()
        alpha = 1
        if not self.plot_density:
            alpha = 0
        self.contour_plot = plt.contourf(
            Burrows.kernel[0],
            Burrows.kernel[1],
            Burrows.normalized_density,
            100,
            cmap=new_hot_r,
            alpha=alpha,
        )

    def plot_coast(self, Burrows):
        self._calculate_countourn_plot(Burrows)
        plt.plot(Burrows.costa_islote.x, Burrows.costa_islote.y, "k", linewidth=1)
        if self.plot_density:
            set_density_colorbar(Burrows.normalized_density, self.contour_plot)

    def plot_sea(self, Burrows):
        fillout(
            Burrows.costa_islote.x,
            Burrows.costa_islote.y,
            limits=[
                Burrows.margen_x[0],
                Burrows.margen_x[1],
                Burrows.margen_y[0],
                Burrows.margen_y[1],
            ],
            color=sea_color,
        )
        self._plot_points(Burrows)

    def _with_points(self):
        with_points = self.explicit_points_dictionary["Show Points"] == "Yes"
        return with_points

    def _plot_points(self, Burrows):
        if self._with_points():
            plt.plot(
                Burrows.east_coordinates,
                Burrows.north_coordinates,
                "o",
                markeredgecolor="k",
            )

    def pimp_plot(self, Burrows):
        plt.xlim(Burrows.margen_x)
        plt.ylim(Burrows.margen_y)
        self.set_map_tick_labels(Burrows, fontsize=20)
        set_scale_bar(
            Burrows.ax,
            Burrows.bar_length,
            Burrows.bar_width,
            loc=Burrows.scale_location,
        )
        Burrows.fig.figimage(self.rose_wind, Burrows.img_x, Burrows.img_y, zorder=100)
        self._set_axes()
        Burrows.ax.tick_params(direction="in")

    def set_map_tick_labels(self, Burrows, fontsize=15):
        ejes = plt.gca()
        y_min, y_max = ejes.get_ylim()
        plt.yticks(
            [
                int(limite)
                for i_limite, limite in enumerate(np.linspace(y_min, y_max, 5))
                if i_limite > 0
            ],
            [
                f"{limite:.0f} mN" if i_limite == 4 else int(limite)
                for i_limite, limite in enumerate(np.linspace(y_min, y_max, 5))
                if i_limite > 0
            ],
            fontsize=fontsize,
        )

        ejes = plt.gca()
        x_min, x_max = ejes.get_xlim()
        plt.xticks(
            [
                int(limite)
                for i_limite, limite in enumerate(
                    np.linspace(x_min, x_max, Burrows.number_of_xticks)
                )
            ],
            [
                f"{limite:.0f} mE" if i_limite == Burrows.number_of_xticks - 1 else int(limite)
                for i_limite, limite in enumerate(
                    np.linspace(x_min, x_max, Burrows.number_of_xticks)
                )
            ],
            fontsize=fontsize,
        )

    def _set_axes(self):
        ejes = plt.gca()
        for label in ejes.yaxis.get_ticklabels():
            label.set_verticalalignment("center_baseline")
        for label in ejes.xaxis.get_ticklabels():
            label.set_horizontalalignment("center")

    def save_plot(self):
        plt.savefig(self.mapa_densidad_ruta, dpi=300, bbox_inches="tight")
