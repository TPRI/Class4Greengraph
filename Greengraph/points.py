__author__ = 'Timothy Rose-Innes'

from numpy import linspace


def location_sequence(start, end, steps):

    lats = linspace(start[0], end[0], steps)
    longs = linspace(start[1], end[1], steps)

    return zip(lats, longs)
