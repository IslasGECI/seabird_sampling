import numpy as np

from geci_plots import roundup


def rounded_ticks_array(superior_limit):
    ticks_array = np.arange(
        0,
        roundup(superior_limit * 1.2, 10),
        roundup(superior_limit * 0.2, 10),
    )
    return ticks_array
