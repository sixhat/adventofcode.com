# %% Load Data
# 
# https://adventofcode.com/2023
# https://docs.python.org/3/

from aoc import *
import numpy as np

data = open("demo.txt", "r").read().strip().splitlines()
pprint(data)
dims = (len(data), len(data[0]))
print(dims)
npd = np.zeros(dims, dtype=int)

