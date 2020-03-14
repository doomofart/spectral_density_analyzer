import csv
import os
import pandas
import numpy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

PATH = config.get('GLOBAL', 'PATH')
FILENAME = PATH.split('/')[-1]


def write_output(frequency, spectral_density, method, window=None):
    col1, col2 = [], []
    for elem in frequency:
        col1.append(str(elem).replace('.', ','))
    for elem in spectral_density:
        col2.append(str(elem).replace('.', ','))
    filename = FILENAME.split('.')[0]
    data = dict(col1=col1, col2=col2)
    frame = pandas.DataFrame(data)
    if not os.path.exists('output'):
        os.mkdir('output')
    if window is not None:
        frame.to_csv('output/%s_%s_%s_out.csv' % (filename, method, window), index=False, sep='\t', header=False)
    else:
        frame.to_csv('output/%s_%s_out.csv' % (filename, method), index=False, sep='\t', header=False)


x_values, y_values = [], []

with open(PATH, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    col_num = len(next(reader))
    if col_num >= 2:
        for row in reader:
            x_values.append(float(row[0].replace(',', '.')))
            y_values.append(float(row[1].replace(',', '.')))
    else:
        for row in reader:
            y_values.append(float(row[0].replace(',', '.')))
        x_values = numpy.linspace(0, len(y_values) / 5000., len(y_values))
