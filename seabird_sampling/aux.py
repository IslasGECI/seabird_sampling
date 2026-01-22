class GeciCliOptions:
    def __init__(
        self,
        data_path,
        input_data_type,
        coast_line_path,
        islet,
        species,
        season,
        wind_rose_path,
        points_option,
        output_path,
    ):
        self.input = [
            [input_data_type],
            [data_path],
            [coast_line_path],
            [islet],
            [species],
            [season],
            [wind_rose_path],
            [points_option],
        ]
        self.output = [[output_path]]
        self.coast_line_path = coast_line_path
        self.input_data_type = input_data_type
        self.data_path = data_path
        self.islet = islet
        self.species = species
        self.season = season
        self.wind_rose_path = wind_rose_path
        self.points_option = points_option
        self.output_path = output_path
