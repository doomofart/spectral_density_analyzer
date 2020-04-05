import os
import sys
import pandas as pd
import logger as error
from functions import initial_signal, welch
from charts import *


class ExcelBuilder(object):
    def __init__(self, cfg, section):
        self.cfg = cfg
        self.section = section
        self.path = self.cfg.get(section, 'PATH')
        self.window = self.cfg.get(section, 'WINDOW')
        self.filtering = self.cfg.get(section, 'FILTERING')

    def filtered_frequency(self):
        filtered_frequency = int(self.cfg.get(self.section, 'FILTERED_FREQUENCY'))
        return filtered_frequency

    def reader(self):
        reader = pd.read_csv(self.path, header=None, delimiter='\t')
        col_num = reader.shape[1]
        if col_num >= 2:
            return reader
        else:
            reader[1] = reader[0]
            reader[0] = reader.index.values
            return reader

    def writer(self):
        filename = self.path.split('/')[-1]
        filename = filename.split('.')[0]
        if not os.path.exists('output'):
            os.mkdir('output')
        if self.filtering == '1':
            writer = pd.ExcelWriter('output/%s_%s_%s.xlsx' % (filename, self.window, self.filtered_frequency()),
                                    engine='xlsxwriter')
        elif self.filtering == '0':
            writer = pd.ExcelWriter('output/%s_%s.xlsx' % (filename, self.window), engine='xlsxwriter')
        else:
            error.value_error(self.section, 'FILTERING')
            sys.exit()
        return writer

    def time_series(self):
        time_series = self.reader()
        if self.filtering == '1':
            data = initial_signal(time_series, filtering=True,
                                  filtered_frequency=self.filtered_frequency())
        elif self.filtering == '0':
            data = initial_signal(time_series)
        else:
            error.value_error(self.section, 'FILTERING')
            sys.exit()
        return data

    def write_output(self):
        writer = self.writer()

        time_series_frame = pd.DataFrame(self.time_series())
        len_time_series_frame = len(time_series_frame.index)
        values = time_series_frame['y']

        spectral_density_frame = pd.DataFrame(welch(values, window=self.window))
        len_spectral_density_frame = len(spectral_density_frame.index)

        time_series_frame.to_excel(writer, index=None, sheet_name='TimeSeries')
        spectral_density_frame.to_excel(writer, index=None, sheet_name='SpectralDensity')

        workbook = writer.book
        chart_time_series(writer, workbook, len_time_series_frame)
        chart_spectral_density(writer, workbook, len_spectral_density_frame)
        chart_spectral_density_log(workbook, len_spectral_density_frame)

        writer.save()
