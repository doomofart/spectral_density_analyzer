import csv
import numpy.fft
import matplotlib.pyplot as plt

x_values, y_values = [], []

with open('Poland_interp_v.dat', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        if row:
            x_values.append(float(row[0].replace(',', '.')))
            y_values.append(float(row[1].replace(',', '.')))

plt.plot(x_values, y_values)

plt.title('Time Series Chart', fontsize=12)
plt.xlabel('t', fontsize=12)
plt.ylabel('Value',fontsize=12)
plt.tick_params(axis='both', labelsize=8)

plt.axis([min(x_values), max(x_values), min(y_values), max(y_values)])

plt.show()

signal = numpy.array(y_values, dtype=float)
n = signal.size

spectral_density, frequency = [], []

spectral_density_total = abs(numpy.fft.fft(y_values))
frequency_total = (numpy.fft.fftfreq(n))

for i in range(len(frequency_total)):
    if frequency_total[i] >= 0:
        spectral_density.append(spectral_density_total[i])
        frequency.append(frequency_total[i])

plt.scatter(frequency, spectral_density, c='blue', s = 5)
plt.plot(frequency, spectral_density, linewidth=1)
plt.title('Spectral Density Chart', fontsize=12)
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Spectral Destiny',fontsize=12)
plt.tick_params(axis='both', labelsize=8)
plt.axis([min(frequency), max(frequency), min(spectral_density), max(spectral_density)])

for i in range(len(spectral_density)):
    print('SD: {0} \nFreq: {1}'.format(spectral_density[i], frequency[i]))
print(str(len(spectral_density)) + ' cases')

plt.show()

