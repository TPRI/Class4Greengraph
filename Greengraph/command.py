__author__ = 'Timothy Rose-Innes'

from argparse import ArgumentParser
from greengrapher import greengrapher

def process():
   parser = ArgumentParser(description = "Plot graph of green spaces between two locations")

   # parser.add_argument('--title', '-t')
   # parser.add_argument('--polite', '-p', action="store_true")
   parser.add_argument('location1')
   parser.add_argument('location2')

   arguments = parser.parse_args()

   greengrapher(arguments.location1, arguments.location2)

if __name__ == "__main__":
    process()
