__author__ = 'Timothy Rose-Innes'

from geolocation import geolocate
from url import map_at
from png_image import count_green_in_png
from points import location_sequence
from visualise import show_green_in_png

def greengrapher(location1, location2):

    # Create a plot of the green spaces around location1
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open('green.png','w') as green:
        green.write(show_green_in_png(map_at(*geolocate(location1),
            zoom=10,satellite=True)))

    # Create a plot to describe the variation in green space between location1 and location2
    plt.plot([
        count_green_in_png(
            map_at(*location,zoom=10,satellite=True))
              for location in location_sequence(
                  geolocate(location1),
                  geolocate(location2),10)])
    plt.savefig('greengraph.png')

