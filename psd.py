import numpy.fft
import graph
from scipy import signal
import file_processing as fp
import configparser
import logger

config = configparser.ConfigParser()
config.read('config.ini')


def initial_signal(x_values, y_values):
    section = 'INITIAL_SIGNAL'
    if config.get(section, 'PLOT_SHOW') == '1':
        graph.time_series(x_values, y_values)
    elif config.get(section, 'PLOT_SHOW') != '0':
        logger.value_error(section)
    return None


def custom(values):
    section = 'CUSTOM'
    spectral_density, frequency = [], []
    spectral_density_total = abs(numpy.fft.fft(values))
    frequency_total = (numpy.fft.fftfreq(len(values)))
    for i in range(len(frequency_total)):
        if frequency_total[i] >= 0:
            spectral_density.append(spectral_density_total[i])
            frequency.append(frequency_total[i])
    if config.get(section, 'OUTPUT_SAVE') == '1':
        fp.write_output(frequency, spectral_density, section.lower())
    elif config.get(section, 'OUTPUT_SAVE') != '0':
        logger.value_error(section)
    if config.get(section, 'PLOT_SHOW') == '1':
        graph.psd(frequency, spectral_density)
    elif config.get(section, 'PLOT_SHOW') != '0':
        logger.value_error(section)
    return None


def welch(values):
    section = 'WELCH'
    spectral_density_welch = signal.welch(values, fs=1.0, scaling='density', window='hamming', nperseg=len(values))
    frequency = spectral_density_welch[0]
    spectral_density = spectral_density_welch[1]
    if config.get(section, 'OUTPUT_SAVE') == '1':
        fp.write_output(frequency, spectral_density, section.lower())
    elif config.get(section, 'OUTPUT_SAVE') != '0':
        logger.value_error(section)
    if config.get(section, 'PLOT_SHOW') == '1':
        graph.psd(frequency, spectral_density)
    elif config.get(section, 'PLOT_SHOW') != '0':
        logger.value_error(section)
    return None


def periodogram(values):
    section = 'PERIODOGRAM'
    spectral_density_period = signal.periodogram(values, fs=1.0, scaling='density', window="hamming")
    frequency = spectral_density_period[0]
    spectral_density = spectral_density_period[1]
    if config.get(section, 'OUTPUT_SAVE') == '1':
        fp.write_output(frequency, spectral_density, section.lower())
    elif config.get(section, 'OUTPUT_SAVE') != '0':
        logger.value_error(section)
    if config.get(section, 'PLOT_SHOW') == '1':
        graph.psd(frequency, spectral_density)
    elif config.get(section, 'PLOT_SHOW') != '0':
        logger.value_error(section)
    return None
