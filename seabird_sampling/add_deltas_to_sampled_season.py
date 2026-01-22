import pandas as pd

from .calculate_order_magnitude import calculate_order_magnitude, round_by_order


def add_intervals_to_sampled_season(barras_error_df, results):
    results["Temporada"] = results["Temporada"].astype(int)
    errors_and_central = get_intervals_from_error_bars_and_series(barras_error_df, results)
    write_intervals_string(errors_and_central)
    joined_df = join_exhaustive_and_sampling_with_intervals(results, errors_and_central)
    return add_percentage_error(joined_df, errors_and_central)


def add_percentage_error(joined_exhaustive_and_sampling, errors_and_central_df):
    df_with_percentage_error = calculate_percentage_error(errors_and_central_df)

    joined = joined_exhaustive_and_sampling.set_index("Temporada").join(
        df_with_percentage_error.set_index("temporada"), rsuffix="right_"
    )
    joined_cutted = joined[["Cantidad de nidos", "percentage_error"]].reset_index()
    return joined_cutted.fillna(0).astype({"percentage_error": int}).replace(0, "-")


def join_exhaustive_and_sampling_with_intervals(exhaustive_df, errors_and_central_sampling):
    errors_and_central_sampling_renamed = errors_and_central_sampling.rename(
        columns={"temporada": "Temporada"}
    )
    concatenated = pd.concat(
        [
            exhaustive_df.set_index("Temporada").astype(int),
            errors_and_central_sampling_renamed.set_index("Temporada"),
        ],
        join="inner",
    )
    return (
        concatenated.reset_index()
        .drop_duplicates(subset="Temporada", keep="last")
        .sort_values("Temporada", ignore_index=True)
    )


def get_intervals_from_error_bars_and_series(barras_error_df, cantidad_nidos):
    merged_df = pd.merge(barras_error_df, cantidad_nidos, left_on="temporada", right_on="Temporada")
    return merged_df.drop(columns=["Temporada"]).rename(columns={"Cantidad de nidos": "central"})


def write_intervals_string(errors_and_central):
    error_bars_list = [
        errors_and_central["minimo"].to_list(),
        errors_and_central["maximo"].to_list(),
    ]
    order_magnitude = calculate_order_magnitude(error_bars_list)
    inferior = errors_and_central["central"] - errors_and_central["minimo"]
    superior = errors_and_central["central"] + errors_and_central["maximo"]
    errors_and_central["central"] = round_by_order(errors_and_central["central"], order_magnitude)
    errors_and_central["inferior"] = round_by_order(inferior, order_magnitude)
    errors_and_central["superior"] = round_by_order(superior, order_magnitude)
    errors_and_central["Cantidad de nidos"] = errors_and_central.apply(
        lambda row: f"{int(row['central'])} ({int(row['inferior'])} - {int(row['superior'])})",
        axis=1,
    )
    return errors_and_central.loc[:, ["temporada", "Cantidad de nidos"]].rename(
        columns={"temporada": "Temporada"}
    )


def calculate_percentage_error(errors_and_central_df):
    errors_and_central_df["percentage_error"] = (
        100
        * (errors_and_central_df.minimo + errors_and_central_df.maximo)
        / (2 * errors_and_central_df.central)
    )
    return errors_and_central_df.round()
