import pandas as pd


def count_total_burrows_per_season(burrows_data, species, colony):
    filtered_burrows = filter_per_specie_and_colony(burrows_data, species, colony)
    return count_burrows(filtered_burrows)


def filter_per_specie_and_colony(burrows_data, especie, colonia):
    return burrows_data[
        (burrows_data.Sitio_o_colonia.str.contains(colonia)) & (burrows_data.Especie == especie)
    ].copy()


def count_burrows(burrows_data):
    splited_season = burrows_data.Temporada.astype(str).str.split("-")
    burrows_data.loc[:, ("Temporada")] = [season[-1] for season in splited_season]
    total_burrows = burrows_data.groupby("Temporada")["ID_madriguera"].count()
    dataframe = pd.DataFrame({"Total_nidos": total_burrows})
    return dataframe
