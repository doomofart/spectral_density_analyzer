import os
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

PATH = config.get('GLOBAL', 'PATH')
FILENAME = PATH.split('/')[-1]


def write_output(frequency, spectral_density, method, window=None):
    filename = FILENAME.split('.')[0]
    data = dict(col1=frequency, col2=spectral_density)
    frame = pd.DataFrame(data)
    if not os.path.exists('output'):
        os.mkdir('output')
    if window is not None:
        frame.to_csv('output/%s_%s_%s_out.csv' % (filename, method, window), index=False, sep='\t', header=False)
    else:
        frame.to_csv('output/%s_%s_out.csv' % (filename, method), index=False, sep='\t', header=False)


with open(PATH, 'r') as file:
    reader = pd.read_csv(file, header=None, delimiter='\t')
    col_num = reader.shape[1]
    if col_num >= 2:
        x_values = reader[0][:]
        y_values = reader[1][:]
    else:
        y_values = reader[0][:]
        x_values = reader.index.values
