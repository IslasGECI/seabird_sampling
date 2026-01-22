from muestreo_aves_marinas_ipbc import GeciCliOptions

islet = "Zapato"
species = "Puffinus opisthomelas"
season = "2018"
wind_rose_path = "rosewind.png"
points_option = "{'Show Points': 'No'}"
output_path = "tests/data/figures.png"


def test_geci_cli_named_options() -> None:
    input_data_type: str = "Burrows"
    coast_line_path = "some_path.shp"
    data_path = "tests/data/nidos_busqueda_aves_marinas_tests.csv"
    paths = GeciCliOptions(
        data_path,
        input_data_type,
        coast_line_path,
        islet,
        species,
        season,
        wind_rose_path,
        points_option,
        output_path,
    )
    assert paths.input_data_type == input_data_type
    assert paths.data_path == data_path
    assert paths.coast_line_path == coast_line_path
    assert paths.islet == islet
    assert paths.species == species
    assert paths.season == season
    assert paths.wind_rose_path == wind_rose_path
    assert paths.points_option == points_option
    assert paths.output_path == output_path


def test_geci_cli_inputs() -> None:
    input_data_type: str = "Quadrants"
    coast_line_path = "other_path.shp"
    data_path = "tests/data/madrigueras_cuadrantes_avesmarinas_test.csv"
    paths = GeciCliOptions(
        data_path,
        input_data_type,
        coast_line_path,
        islet,
        species,
        season,
        wind_rose_path,
        points_option,
        output_path,
    )
    assert paths.input[0][0] == input_data_type
    assert paths.input[1][0] == data_path
    assert paths.input[2][0] == coast_line_path
    assert paths.input[3][0] == islet
    assert paths.input[4][0] == species
    assert paths.input[5][0] == season
    assert paths.input[6][0] == wind_rose_path
    assert paths.input[7][0] == points_option
    assert paths.output[0][0] == output_path
