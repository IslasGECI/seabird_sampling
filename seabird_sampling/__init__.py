"""A Python module for seabird sampling processing"""

__version__ = "0.5.1"
from .add_deltas_to_sampled_season import (  # noqa
    add_intervals_to_sampled_season,
    get_intervals_from_error_bars_and_series,
)
from .BurrowsIntervals import BurrowSeries, write_error_bars_json  # noqa
from .calculate_nesting_zone_from_kml import (  # noqa
    get_latitude_from_kml,
    get_longitude_from_kml,
    read_kml_features,
)
from .max_min_from_dataframe import combine_error_bars, max_min_from_dataframe  # noqa
from .plot_error_bar import get_table_salida, plot_error_bars, make_sure_folder_exists  # noqa
from .plot_exhaustive_searches import plot_exhaustive_searches  # noqa
from .Plotter_Burrows import Plotter_Burrows  # noqa
from .total_burrows import get_cantidad_nidos  # noqa
