# %% Load Data
#
# https://adventofcode.com/2023
# https://docs.python.org/3/

from matplotlib import pyplot as plt
from aoc import pprint
import numpy as np
import sys

sys.setrecursionlimit(10000)

data = open("input.txt", "r").read().strip().splitlines()
dims = (len(data), len(data[0]))
path = [np.zeros(2, dtype=int)]

Ds = {
    "R": np.array([0, 1], dtype=int),
    "D": np.array([1, 0], dtype=int),
    "L": np.array([0, -1], dtype=int),
    "U": np.array([-1, 0], dtype=int),
}


for line in data:
    D, n, c = line.split()
    n = int(n)
    while n > 0:
        path.append(path[-1] + Ds[D])
        n -= 1

# neste instante temos uma path, agora falta encher. A direção
# será dada pela mão esquerda ou direita conforme os cassos
a = int(max([x[0] for x in path]))
b = int(min([x[0] for x in path]))
c = int(max([x[1] for x in path]))
d = int(min([x[1] for x in path]))

npd = np.zeros((1 + a - b, 1 + c - d), dtype=int)
for p in path:
    npd[p[0] - b, p[1] - d] = 1

plt.imshow(npd, interpolation="none")
plt.show()


# Diffusion then
def dif(r, c):
    if npd[r, c] == 0 and 0 < r < npd.shape[0] and 0 < c < npd.shape[1]:
        npd[r, c] = 1
        dif(r, c + 1)
        dif(r, c - 1)
        dif(r - 1, c)
        dif(r + 1, c)
    else:
        return
    
dif(150,100)

plt.imshow(npd, interpolation="none")
plt.show()

print('-- Total part A:\t', np.sum(npd))
