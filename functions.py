import prox_tv as ptv
from scipy import signal


def initial_signal(x_values, y_values, filtering=False, filtered_frequency=None):
    if filtering:
        y_values = ptv.tv1_1d(y_values, filtered_frequency)
    return dict(x=x_values, y=y_values)


def welch(values, window='hamming'):
    spectral_density_welch = signal.welch(values, fs=1.0, scaling='density', window=window,
                                          nperseg=len(values))
    frequency = spectral_density_welch[0]
    spectral_density = spectral_density_welch[1]
    return dict(frequency=frequency, spectral_density=spectral_density)
