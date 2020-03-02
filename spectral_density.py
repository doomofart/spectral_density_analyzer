import graph
import psd
import file_processing as fp

x_values, y_values = fp.x_values, fp.y_values

graph.time_series(x_values, y_values)

psd.custom(y_values)
psd.welch(y_values)
psd.periodogram(y_values)
