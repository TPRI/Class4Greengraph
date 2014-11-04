__author__ = 'Timothy Rose-Innes'

#TODO: Tidy up main code (perhaps separate out save into a module)
#TODO: Create an executable script to pass inputs to greengrapher module

from geolocation import geolocate
from url import map_at
from png_image import count_green_in_png
from points import location_sequence
from visualise import show_green_in_png

def greengrapher(location1, location2):

    london_location = geolocate(location1)

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
                  geolocate(location1),
                  geolocate(location2),10)])
    plt.savefig('greengraph.png')

