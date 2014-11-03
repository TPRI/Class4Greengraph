__author__ = 'Timothy Rose-Innes'

def geolocation(place):

    import geopy

    geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

    location = geocoder.geocode(place, exactly_one=False)[0][1]

    return location

