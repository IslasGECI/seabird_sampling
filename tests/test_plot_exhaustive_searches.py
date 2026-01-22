from muestreo_aves_marinas_ipbc import plot_exhaustive_searches

import pandas as pd
import os


def test_plot_exhaustive_searches():
    exhaustive_data = pd.read_csv("tests/data/total_nidos_temporada_mergulo_punta_sur.csv")
    output_path = "tests/data/exhaustive_searches_plot.png"
    if os.path.exists(output_path):
        os.remove(output_path)
    plot_exhaustive_searches(exhaustive_data, output_path)
    assert os.path.exists(output_path)
