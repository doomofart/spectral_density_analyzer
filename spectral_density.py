import psd
import file_processing as fp

x_values, y_values = fp.x_values, fp.y_values

psd.initial_signal(x_values, y_values)
psd.custom(y_values)
psd.welch(x_values, y_values, y_values)
psd.periodogram(y_values)
