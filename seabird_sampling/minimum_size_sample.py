import scipy.stats


def calculate_sample_size_for_an_error_of(quadrants_data, percentage_error):
    decimal_percentage_error = percentage_error / 100
    quantile = 0.975
    sampling_size = (
        (
            scipy.stats.t.ppf(quantile, 10_000)
            * quadrants_data.Madrigueras_con_actividad_aparente.std()
        )
        / (decimal_percentage_error * quadrants_data.Madrigueras_con_actividad_aparente.mean())
    ) ** 2
    return round(sampling_size)


def calculate_variation_coefficient(quadrants_data):
    variation_coefficient = (
        quadrants_data.Madrigueras_con_actividad_aparente.std()
        / quadrants_data.Madrigueras_con_actividad_aparente.mean()
    )
    if variation_coefficient > 0.75:
        raise ValueError(
            "Coeficiente de variación muy alto. Necesitamos tamaño de la muestra > 220"
        )
    print(variation_coefficient)
    return variation_coefficient
