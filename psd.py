import prox_tv as ptv
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
    if config.get(section, 'FILTER') == '1':
        filtered_frequency = config.get(section, 'FILTERED_FREQUENCY')
        y_values = ptv.tv1_1d(y_values, filtered_frequency)
    return dict(x=x_values, y=y_values)


def welch(x, y, values):
    section = 'WELCH'
    window = config.get(section, 'WINDOW')
    spectral_density_welch = signal.welch(values, fs=1.0, scaling='density', window=window,
                                          nperseg=len(values))
    frequency = spectral_density_welch[0]
    spectral_density = spectral_density_welch[1]
    if config.get(section, 'OUTPUT_SAVE') == '1':
        fp.write_output(x, y, frequency, spectral_density, section.lower(), window)
    elif config.get(section, 'OUTPUT_SAVE') != '0':
        logger.value_error(section)
    if config.get(section, 'PLOT_SHOW') == '1':
        graph.psd(frequency, spectral_density)
    elif config.get(section, 'PLOT_SHOW') != '0':
        logger.value_error(section)
    return dict(frequency=frequency, spectral_density=spectral_density)
