import csv
import pandas
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

FILENAME = config.get('GLOBAL', 'FILENAME')


def write_output(frequency, spectral_density, method, window=None):
    col1, col2 = [], []
    for elem in frequency:
        col1.append(str(elem).replace('.', ','))
    for elem in spectral_density:
        col2.append(str(elem).replace('.', ','))
    filename = FILENAME.split('.')[0]
    data = dict(col1=col1, col2=col2)
    frame = pandas.DataFrame(data)
    if window is not None:
        frame.to_csv('%s_%s_%s_out.csv' % (filename, method, window), index=False, sep='\t', header=False)
    else:
        frame.to_csv('%s_%s_out.csv' % (filename, method), index=False, sep='\t', header=False)


x_values, y_values = [], []

with open(FILENAME, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        if row:
            x_values.append(float(row[0].replace(',', '.')))
            y_values.append(float(row[1].replace(',', '.')))
