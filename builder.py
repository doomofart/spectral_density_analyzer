import os
import pandas as pd


class ExcelBuilder(object):
    def __init__(self, cfg, section):
        self.cfg = cfg
        self.section = section

    def file_reader(self):
        path = self.cfg.get(self.section, 'PATH')
        reader = pd.read_csv(path, header=None, delimiter='\t')
        col_num = reader.shape[1]
        if col_num >= 2:
            return reader
        else:
            y_values = reader[0][:]
            x_values = reader.index.values
            return pd.DataFrame(x_values, y_values)

    def write_output(self, x_values, y_values, frequency, spectral_density, method, window=None):
        FILENAME = PATH.split('/')[-1]
        filename = self.FILENAME.split('.')[0]
        data = dict(frequency=frequency, spectral_density=spectral_density)
        frame = pd.DataFrame(data)
        len_frame = len(frame.index)

        # trash
        data_1 = dict(x=x_values, y=y_values)
        frame_1 = pd.DataFrame(data_1)
        len_frame_1 = len(frame_1.index)

        if not os.path.exists('output'):
            os.mkdir('output')
        if window is not None:
            writer = pd.ExcelWriter('output/%s_%s_%s_out.xlsx' % (filename, method, window), engine='xlsxwriter')
        else:
            writer = pd.ExcelWriter('output/%s_%s_out.xlsx' % (filename, method), engine='xlsxwriter')

        # trash
        frame_1.to_excel(writer, index=None, sheet_name='TimeSeries')

        frame.to_excel(writer, index=None, sheet_name='SpectralDensity')

        workbook = writer.book

        # trash
        worksheet = writer.sheets['TimeSeries']
        time_series_chart = workbook.add_chart({'type': 'scatter'})
        time_series_chart.add_series({
            'categories': ['TimeSeries', 1, 0, len_frame_1, 0],
            'values': ['TimeSeries', 1, 1, len_frame_1, 1],
        })
        time_series_chart.set_x_axis({'name': 'x', 'position_axis': 'on_tick'})
        time_series_chart.set_y_axis({'name': 'y', 'num_format': '0.00E+00', 'major_gridlines': {'visible': False}})
        time_series_chart.set_legend({'position': 'none'})
        time_series_chart.set_size({'width': 640, 'height': 480})
        worksheet.insert_chart('D2', time_series_chart)

        worksheet = writer.sheets['SpectralDensity']
        spectral_density_chart = workbook.add_chart({'type': 'scatter'})
        spectral_density_chart.add_series({
            'categories': ['SpectralDensity', 1, 0, len_frame, 0],
            'values': ['SpectralDensity', 1, 1, len_frame, 1],
        })
        spectral_density_chart.set_x_axis({'name': 'Frequency', 'major_unit': 0.1, 'minor_unit': 0.01, 'max': 0.5,
                          'position_axis': 'on_tick'})
        spectral_density_chart.set_y_axis({'name': 'Spectral Density', 'num_format': '0.00E+00', 'major_gridlines': {'visible': False}})
        spectral_density_chart.set_legend({'position': 'none'})
        spectral_density_chart.set_size({'width': 640, 'height': 480})
        worksheet.insert_chart('D2', spectral_density_chart)

        worksheet = workbook.add_worksheet('SpectralDensityLog')
        spectral_density_log_chart = workbook.add_chart({'type': 'scatter'})
        spectral_density_log_chart.add_series({
            'categories': ['SpectralDensity', 2, 0, len_frame, 0],
            'values': ['SpectralDensity', 2, 1, len_frame, 1],
            'trendline': {
                'type': 'power',
                'display_equation': True,
                'display_r_squared': True}
        })
        spectral_density_log_chart.set_x_axis({'name': 'Frequency (log)',
                                               'log_base': 10,
                                               'major_unit': 0.1,
                                               'minor_unit': 0.01,
                                               'max': 0.5,
                                               'position_axis': 'on_tick'})
        spectral_density_log_chart.set_y_axis(
            {'name': 'Spectral Density (log)', 'log_base': 10, 'num_format': '0.00E+00',
             'major_gridlines': {'visible': False}})
        spectral_density_log_chart.set_legend({'position': 'none'})
        spectral_density_log_chart.set_size({'width': 640, 'height': 480})
        worksheet.insert_chart('D2', spectral_density_log_chart)

        writer.save()

