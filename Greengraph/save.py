__author__ = 'Timothy'

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open('green.png', 'w') as green:
    green.write(show_green_in_png(map_at(*london_location,
        zoom=10,satellite=True)))

plt.plot([
    count_green_in_png(
        map_at(*location, zoom=10, satellite=True))
            for location in location_sequence(
              geolocate("London"),
              geolocate("Birmingham"),10)])

plt.savefig('greengraph.png')