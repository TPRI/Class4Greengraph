# Unit tests for is_green module in png_image file

from nose.tools import assert_true, assert_false
from Geolocate.png_image import is_green

# Give the module input parameters (r,g,b) that are required to pass and fail
def test_is_green():
    assert_true(is_green(1,2,1))
    assert_false(is_green(2,1,1))