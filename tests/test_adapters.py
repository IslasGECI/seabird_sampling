from seabird_sampling.adapters import adapt_historical_data
import pandas as pd


def test_adapt_historical_data():
    historical_data = pd.DataFrame(
        {
            "Species_name": [
                "Laysan Albatross",
                "Laysan Albatross",
                "Laysan Albatross",
                "Guadalupe Murrelet",
            ],
            "Island": ["Guadalupe", "Guadalupe", "Morro Prieto and Zapato", "Guadalupe"],
            "Season": [2015, 2016, 2020, 2015],
            "Maximum_number_of_nests": [20, 30, 1000, 100],
        }
    )
    obtained = adapt_historical_data(historical_data)
    expected_column_names = ["Especie", "Sitio_o_colonia", "Temporada", "Total_nidos"]
    assert all(obtained.columns in expected_column_names)
