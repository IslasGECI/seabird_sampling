from seabird_sampling.calculate_order_magnitude import calculate_order_magnitude, round_by_order

import numpy as np


def test_calculate_order_magnitude():
    error_bars = [[1, 800], [10, 900]]
    obtained_order = calculate_order_magnitude(error_bars)
    expected_order = 10
    assert obtained_order == expected_order

    error_bars = [[1, 80], [10, 91]]
    obtained_order = calculate_order_magnitude(error_bars)
    expected_order = 1
    assert obtained_order == expected_order

    error_bars = [[45, 80], [155, 91]]
    obtained_order = calculate_order_magnitude(error_bars)
    expected_order = 10
    assert obtained_order == expected_order

    error_bars = [[156, 80], [62, 91]]
    obtained_order = calculate_order_magnitude(error_bars)
    expected_order = 10
    assert obtained_order == expected_order


def test_round_by_order():
    order = 10
    number = 4819
    obtained = round_by_order(number, order)
    expected = 4820
    assert obtained == expected

    order = 100
    number = 2050
    obtained = round_by_order(number, order)
    expected = 2000
    assert obtained == expected
    number = 2051
    obtained = round_by_order(number, order)
    expected = 2100
    assert obtained == expected

    number = np.array([2051])
    obtained = round_by_order(number, order)
    expected = 2100
    assert obtained == expected
