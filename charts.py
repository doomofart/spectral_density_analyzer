MARKER = {'type': 'circle', 'size': 4, 'border': {'color': 'blue'}, 'fill': {'color': 'white'}}


def chart_time_series(writer, workbook, values_num):
    worksheet = writer.sheets['TimeSeries']
    time_series_chart = workbook.add_chart({'type': 'scatter'})
    time_series_chart.add_series({
        'categories': ['TimeSeries', 1, 0, values_num, 0],
        'values': ['TimeSeries', 1, 1, values_num, 1],
        'marker': MARKER,
    })
    time_series_chart.set_x_axis({'name': 'x', 'position_axis': 'on_tick'})
    time_series_chart.set_y_axis({'name': 'y', 'num_format': '0.00E+00', 'major_gridlines': {'visible': False}})
    time_series_chart.set_legend({'position': 'none'})
    time_series_chart.set_size({'width': 640, 'height': 480})
    return worksheet.insert_chart('D2', time_series_chart)


def chart_spectral_density(writer, workbook, values_num):
    worksheet = writer.sheets['SpectralDensity']
    spectral_density_chart = workbook.add_chart({'type': 'scatter'})
    spectral_density_chart.add_series({
        'categories': ['SpectralDensity', 1, 0, values_num, 0],
        'values': ['SpectralDensity', 1, 1, values_num, 1],
        'marker': MARKER
    })
    spectral_density_chart.set_x_axis({'name': 'Frequency', 'major_unit': 0.1, 'minor_unit': 0.01, 'max': 0.5,
                                       'position_axis': 'on_tick'})
    spectral_density_chart.set_y_axis(
        {'name': 'Spectral Density', 'num_format': '0.00E+00', 'major_gridlines': {'visible': False}})
    spectral_density_chart.set_legend({'position': 'none'})
    spectral_density_chart.set_size({'width': 640, 'height': 480})
    return worksheet.insert_chart('D2', spectral_density_chart)


def chart_spectral_density_log(workbook, values_num):
    worksheet = workbook.add_worksheet('SpectralDensityLog')
    spectral_density_log_chart = workbook.add_chart({'type': 'scatter'})
    spectral_density_log_chart.add_series({
        'categories': ['SpectralDensity', 2, 0, values_num, 0],
        'values': ['SpectralDensity', 2, 1, values_num, 1],
        'marker': MARKER,
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
    return worksheet.insert_chart('D2', spectral_density_log_chart)