import prox_tv as ptv
from scipy import signal


def initial_signal(frame, filtering=False, filtered_frequency=None):
    x_values, y_values = frame[0], frame[1]
    if filtering:
        y_values = ptv.tv1_1d(y_values, filtered_frequency)
    return dict(x=x_values, y=y_values)


def welch(values, window):
    spectral_density_welch = signal.welch(values, fs=1.0, scaling='density', window=window,
                                          nperseg=len(values))
    frequency = spectral_density_welch[0]
    spectral_density = spectral_density_welch[1]
    return dict(frequency=frequency, spectral_density=spectral_density)
