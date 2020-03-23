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
    if not os.path.exists('output'):
        os.mkdir('output')
    if window is not None:
        writer = pd.ExcelWriter('output/%s_%s_%s_out.xlsx' % (filename, method, window))
    else:
        writer = pd.ExcelWriter('output/%s_%s_out.xlsx' % (filename, method))
    frame.to_excel(writer, index=None)
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
