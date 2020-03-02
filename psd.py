import numpy.fft
import graph
from scipy import signal
import file_processing as fp


def custom(values):
    signal = numpy.array(values, dtype=float)
    n = signal.size
    spectral_density, frequency = [], []
    spectral_density_total = abs(numpy.fft.fft(values))
    frequency_total = (numpy.fft.fftfreq(n))
    for i in range(len(frequency_total)):
        if frequency_total[i] >= 0:
            spectral_density.append(spectral_density_total[i])
            frequency.append(frequency_total[i])
    fp.write_output(frequency, spectral_density, 'custom')
    return graph.psd(frequency, spectral_density)


def welch(values):
    spectral_density_welch = signal.welch(values, fs=1.0, scaling='density', window="hamming", nperseg=470)
    frequency = spectral_density_welch[0]
    spectral_density = spectral_density_welch[1]
    fp.write_output(frequency, spectral_density, 'welch')
    return graph.psd(frequency, spectral_density)


def periodogram(values):
    spectral_density_period = signal.periodogram(values, fs=1.0, scaling='density', window="hamming")
    frequency = spectral_density_period[0]
    spectral_density = spectral_density_period[1]
    fp.write_output(frequency, spectral_density, 'periodogram')
    return graph.psd(frequency, spectral_density)
