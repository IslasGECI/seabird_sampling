import pandas as pd


def concatenate_main_islet_colonies(colony_a, colony_b):
    column_name = "Total_nidos"
    return _sum_by_season(colony_a, colony_b, column_name)


def get_total_burrows(nidos_morro, nidos_punta_sur):
    column_name = "Cantidad de nidos"
    return _sum_by_season(nidos_morro, nidos_punta_sur, column_name)


def _sum_by_season(colony_a, colony_b, column_name):
    concatenated_colonies = concatenate_colonies(colony_a, colony_b)
    return _sum_by_row_and_name_columns(concatenated_colonies, column_name)


def _sum_by_row_and_name_columns(total_nidos, column_name):
    total_nidos = pd.DataFrame(
        {column_name: total_nidos.sum(axis=1), "Temporada": total_nidos.index.values}
    )
    return total_nidos


def concatenate_colonies(nidos_morro, nidos_punta_sur):
    nidos_morro = nidos_morro.set_index("Temporada")
    nidos_punta_sur = nidos_punta_sur.set_index("Temporada")
    total_nidos = pd.concat([nidos_morro, nidos_punta_sur], axis=1).fillna(0)
    return total_nidos.sort_index()


def get_cantidad_nidos(
    datos_nidos_morro, datos_nidos_zapato, ruta_datos_punta_sur, option_only_islets
):
    datos_nidos_morro["Cantidad de nidos"] = (
        datos_nidos_morro["Cantidad de nidos"] + datos_nidos_zapato["Cantidad de nidos"]
    )
    if option_only_islets == "All islets":
        datos_nidos_punta_sur = pd.read_csv(ruta_datos_punta_sur)
        datos_nidos_morro = get_total_burrows(datos_nidos_morro, datos_nidos_punta_sur)
        return datos_nidos_morro
    cantidad_nidos = datos_nidos_morro.set_index("Temporada", drop=False)
    return cantidad_nidos
