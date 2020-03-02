import matplotlib.pyplot as plt


def psd(frequency, spectral_density):
    plt.scatter(frequency, spectral_density, c='blue', s=5)
    plt.plot(frequency, spectral_density, linewidth=1)
    plt.title('Spectral Density Chart', fontsize=12)
    plt.xlabel('Frequency', fontsize=12)
    plt.ylabel('Spectral Destiny', fontsize=12)
    plt.tick_params(axis='both', labelsize=8)
    plt.axis([min(frequency), max(frequency), min(spectral_density), max(spectral_density)])
    return plt.show()


def time_series(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.title('Time Series Chart', fontsize=12)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.tick_params(axis='both', labelsize=8)
    plt.axis([min(x_values), max(x_values), min(y_values), max(y_values)])
    plt.show()
