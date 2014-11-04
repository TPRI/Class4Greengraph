__author__ = 'Timothy Rose-Innes'

#TODO: Define a module
#TODO: Pull out locations into inputs,
#TODO: Tidy up main code (perhaps separate out save into a module)
#TODO: Create an executable script to pass inputs to greengrapher module

from geolocation import geolocate
from url import map_at
from png_image import count_green_in_png
from points import location_sequence
from visualise import show_green_in_png

def greengrapher():

    london_location = geolocate("London")

    ### "save"
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open('green.png','w') as green:
        green.write(show_green_in_png(map_at(*london_location,
            zoom=10,satellite=True)))

    plt.plot([
        count_green_in_png(
            map_at(*location,zoom=10,satellite=True))
              for location in location_sequence(
                  geolocate("London"),
                  geolocate("Birmingham"),10)])
    plt.savefig('greengraph.png')

greengrapher()