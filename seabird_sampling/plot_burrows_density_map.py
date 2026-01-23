import matplotlib.pyplot as plt


def choose_coast_line(islet, linea_costa):
    linea_costa_islote = linea_costa[12]
    margen_superior_isla = 100
    isMorroPrieto = islet == "Morro Prieto"
    if isMorroPrieto:
        linea_costa_islote = linea_costa[1]
        margen_superior_isla = 70
    return linea_costa_islote, margen_superior_isla


def set_plot():
    plt.figure(figsize=(11, 8))
    plt.yticks(rotation=90)
    plt.gca().set_facecolor("#E6FFFF")
    return plt.gcf()
