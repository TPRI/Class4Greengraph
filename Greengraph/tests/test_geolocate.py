# Unit tests for geolocate

from nose.tools import assert_almost_equal
from Greengraph.geolocation import geolocate


# Verify that the coordinates returned agree with previously looked up values
def test_geolocation():
    coordinates = geolocate("Timbuktu")
    assert_almost_equal(coordinates[0], 16.7665887)
    assert_almost_equal(coordinates[1], -3.0025615)
