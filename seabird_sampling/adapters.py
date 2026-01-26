def adapt_historical_data(historical_data_df):
    return historical_data_df.rename(
        columns={
            "Species_name": "Especie",
            "Island": "Sitio_o_colonia",
            "Season": "Temporada",
            "Maximum_number_of_nests": "Total_nidos",
        }
    )
