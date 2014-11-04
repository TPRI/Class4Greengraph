__author__ = 'Timothy Rose-Innes'

from itertools import izip
from StringIO import StringIO
from png_image import is_green
from png import from_array, Reader


def show_green_in_png(data):

    image = Reader(file=StringIO(data.content)).asRGB()

    count = 0
    out = []
    for row in image[2]:
        outrow = []
        pixels = izip(*[iter(row)]*3)
        for pixel in pixels:
            outrow.append(0)
            if is_green(*pixel):
                outrow.append(255)
            else:
                outrow.append(0)
            outrow.append(0)
        out.append(outrow)

    buffer=StringIO()
    result = from_array(out, mode='RGB')
    result.save(buffer)

    return buffer.getvalue()