import csv
import pandas
from config import FILENAME


def write_output(frequency, spectral_density, method):
    filename = FILENAME.split('.')[0]
    data = dict(col1=frequency, col2=spectral_density)
    frame = pandas.DataFrame(data)
    frame.to_csv('%s_%s_out' % (filename, method), index=False, sep='\t', header=False)


x_values, y_values = [], []

with open(FILENAME, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        if row:
            x_values.append(float(row[0].replace(',', '.')))
            y_values.append(float(row[1].replace(',', '.')))
