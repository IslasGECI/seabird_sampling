class Numbers:
    guadalupe_easting_limits: list = [366000, 382000]
    guadalupe_northing_lmits: list = [3191000, 3232000]
    bubble_scale: int = 50


def test_enums():
    assert Numbers.bubble_scale == 50


def test_short_vertion():
    two = 1
    two += 1
    assert two == 2
