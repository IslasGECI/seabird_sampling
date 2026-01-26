import typer
import pandas as pd
from seabird_sampling.adapters import adapt_historical_data
from seabird_sampling.aux import GeciCliOptions
from seabird_sampling.Burrows_in_Islets import ConcreteBurrowsFactory
from seabird_sampling.filter_data import (
    count_total_burrows_per_season,
    filter_per_specie_and_colony,
)
from seabird_sampling.Plotter_Burrows import Plotter_Burrows
from seabird_sampling.total_burrows import concatenate_main_islet_colonies, get_total_burrows

cli = typer.Typer()


@cli.command()
def plot_distribution_map(
    data_path: str = typer.Option(),
    input_data_type: str = typer.Option(),
    coast_line_path: str = typer.Option(default="data/raw/linea_costa_isla_guadalupe.shp"),
    islet: str = typer.Option(),
    species: str = typer.Option(),
    season: str = typer.Option(),
    wind_rose_path: str = typer.Option(default="data/raw/rosewind.png"),
    points_option: str = typer.Option(default='{"Show Points": "Yes"}'),
    output_path: str = typer.Option(),
):
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
    Factory = ConcreteBurrowsFactory(paths)
    Madrigueras = Factory.create_burrows()
    Madrigueras.set_coordinate()
    Madrigueras.calculate_kernel()
    Madrigueras.normalize_density()
    Madrigueras.custom_plot()
    Madrigueras.set_plot_location()
    Graficador = Plotter_Burrows(paths, plot_density=False)
    Graficador.plot_coast(Madrigueras)
    Graficador.plot_sea(Madrigueras)
    Graficador.pimp_plot(Madrigueras)
    Graficador.save_plot()


@cli.command(help="Ayuda de este comando")
def plot_density_map(
    data_path: str = typer.Option(),
    input_data_type: str = typer.Option(),
    coast_line_path: str = typer.Option(default="data/raw/linea_costa_isla_guadalupe.shp"),
    islet: str = typer.Option(),
    species: str = typer.Option(),
    season: str = typer.Option(),
    wind_rose_path: str = typer.Option(default="data/raw/rosewind.png"),
    points_option: str = typer.Option(default='{"Show Points": "No"}'),
    output_path: str = typer.Option(),
):
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
    Factory = ConcreteBurrowsFactory(paths)
    Madrigueras = Factory.create_burrows()
    Madrigueras.set_coordinate()
    Madrigueras.calculate_kernel()
    Madrigueras.normalize_density()
    Madrigueras.custom_plot()
    Madrigueras.set_plot_location()
    Graficador = Plotter_Burrows(paths)
    Graficador.plot_coast(Madrigueras)
    Graficador.plot_sea(Madrigueras)
    Graficador.pimp_plot(Madrigueras)
    Graficador.save_plot()


@cli.command()
def concatenate_burrows_by_season(
    first_colony_path: str = typer.Option("", help="First colony data path"),
    second_colony_path: str = typer.Option("", help="Second colony data path"),
    output_path: str = typer.Option("", help="Output path"),
):
    first_colony_df = pd.read_csv(first_colony_path)
    second_colony_df = pd.read_csv(second_colony_path)
    concatenated_colonies = concatenate_main_islet_colonies(first_colony_df, second_colony_df)
    concatenated_colonies.to_csv(output_path, index=False)


@cli.command()
def concatenate_burrows_by_season_to_cantidad_nidos(
    first_colony_path: str = typer.Option("", help="First colony data path"),
    second_colony_path: str = typer.Option("", help="Second colony data path"),
    output_path: str = typer.Option("", help="Output path"),
):
    first_colony_df = pd.read_csv(first_colony_path)
    second_colony_df = pd.read_csv(second_colony_path)
    concatenated_colonies = get_total_burrows(first_colony_df, second_colony_df)
    concatenated_colonies.to_csv(output_path, index=False)


@cli.command()
def write_burrows_count_by_season(
    data_path: str = typer.Option("", help="Burrows data path"),
    species: str = typer.Option("", help="Species to count"),
    colony: str = typer.Option("", help="Colony to count"),
    output_path: str = typer.Option("", help="Output path"),
):
    burrows_data = pd.read_csv(data_path)
    total_burrows_df = count_total_burrows_per_season(burrows_data, species, colony)
    total_burrows_df.to_csv(output_path)


@cli.command()
def write_historical_burrows_by_species_and_island(
    data_path: str = typer.Option("", help="Burrows data path"),
    species: str = typer.Option("", help="Species to count"),
    colony: str = typer.Option("", help="Colony to count"),
    output_path: str = typer.Option("", help="Output path"),
):
    data_df = pd.read_csv(data_path)
    data_adapted_df = adapt_historical_data(data_df)
    filtered_df = filter_per_specie_and_colony(data_adapted_df, species, colony)
    filtered_df.loc[:, ["Temporada", "Total_nidos"]].to_csv(output_path, index=False)


@cli.command(help="ayuda version")
def version():
    print("0.5.0")
