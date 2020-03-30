import os
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

PATH = config.get('GLOBAL', 'PATH')
FILENAME = PATH.split('/')[-1]


def write_output(frequency, spectral_density, method, window=None):
    filename = FILENAME.split('.')[0]
    data = dict(frequency=frequency, spectral_density=spectral_density)
    frame = pd.DataFrame(data)
    len_frame = len(frame.index)
    if not os.path.exists('output'):
        os.mkdir('output')
    if window is not None:
        writer = pd.ExcelWriter('output/%s_%s_%s_out.xlsx' % (filename, method, window), engine='xlsxwriter')
    else:
        writer = pd.ExcelWriter('output/%s_%s_out.xlsx' % (filename, method), engine='xlsxwriter')
    frame.to_excel(writer, index=None, sheet_name='SpectralDensity')
    
    workbook = writer.book
    worksheet = writer.sheets['SpectralDensity']
    chart = workbook.add_chart({'type': 'scatter'})
    chart.add_series({
        'categories': ['SpectralDensity', 1, 0, len_frame, 0],
        'values': ['SpectralDensity', 1, 1, len_frame, 1],
    })
    chart.set_x_axis({'name': 'Frequency', 'major_unit': 0.1, 'minor_unit': 0.01, 'max': 0.5,
                      'position_axis': 'on_tick'})
    chart.set_y_axis({'name': 'Spectral Density', 'num_format': '0.00E+00', 'major_gridlines': {'visible': False}})
    chart.set_legend({'position': 'none'})
    chart.set_size({'width': 640, 'height': 480})
    worksheet.insert_chart('D2', chart)

    writer.save()


with open(PATH, 'r') as file:
    reader = pd.read_csv(file, header=None, delimiter='\t')
    col_num = reader.shape[1]
    if col_num >= 2:
        x_values = reader[0][:]
        y_values = reader[1][:]
    else:
        y_values = reader[0][:]
        x_values = reader.index.values
