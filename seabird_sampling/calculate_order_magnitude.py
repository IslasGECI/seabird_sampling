from geci_plots import order_magnitude

import numpy as np


def calculate_order_magnitude(error_bars):
    minimums = np.array(error_bars[0])
    maximums = np.array(error_bars[1])
    difference = maximums + minimums
    order = order_magnitude(difference * 0.05)
    return 10**order


def round_by_order(number, order):
    return np.round(number / order) * order
