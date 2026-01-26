def adapt_historical_data(historical_data_df):
    historica_data_renamed = historical_data_df.rename(
        columns={
            "Species_name": "Especie",
            "Island": "Sitio_o_colonia",
            "Season": "Temporada",
            "Maximum_number_of_nests": "Total_nidos",
        }
    )
    species_dictionary = {"Laysan Albatross": "Phoebastria immutabilis"}
    return historica_data_renamed.replace({"Especie": species_dictionary})
