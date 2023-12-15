# https://adventofcode.com/2023
# https://docs.python.org/3/

from aoc import *

data = open("demo.txt", "r").read().strip().splitlines()
pprint(data)


# pprint(rotcw(data))
# pprint(rotccw(data))
pprint(rot180(data))