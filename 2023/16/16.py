# %% Load Data
# https://adventofcode.com/2023/day/16
# https://docs.python.org/3/
# --- Day 16: The Floor Will Be Lava ---
# seems like a Depth First Search.
import sys
import numpy as np
from aoc import *

data = open("input.txt", "r").read().strip().splitlines()
pprint(data)
dims = (len(data), len(data[0]))
print(dims)
npd = np.zeros(dims, dtype=int)
npp = np.zeros(dims, dtype=int)
# print(npd)
# print(npp)
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())

# %% Recursive Solution?

path = []


def move(pos, dir, npd, data, n):
    global npp
    if max(pos) >= dims[0] or min(pos) < 0:
        return
    if npd[pos[0], pos[1]] == dir:
        return
    if n > 12100:
        return

    npp[pos[0], pos[1]] = n
    npd[pos[0], pos[1]] = dir

    path.append(pos)

    nxt = data[pos[0]][pos[1]]

    if dir == 1:
        if nxt == "-":
            move([pos[0], pos[1] - 1], 4, npd, data, n + 1)
            move([pos[0], pos[1] + 1], 2, npd, data, n + 1)
        elif nxt == "\\":
            move([pos[0], pos[1] - 1], 4, npd, data, n + 1)
        elif nxt == "/":
            move([pos[0], pos[1] + 1], 2, npd, data, n + 1)
        else:
            move([pos[0] - 1, pos[1]], 1, npd, data, n + 1)
    elif dir == 2:
        if nxt == "|":
            move([pos[0] - 1, pos[1]], 1, npd, data, n + 1)
            move([pos[0] + 1, pos[1]], 3, npd, data, n + 1)
        elif nxt == "\\":
            move([pos[0] + 1, pos[1]], 3, npd, data, n + 1)
        elif nxt == "/":
            move([pos[0] - 1, pos[1]], 1, npd, data, n + 1)
        else:
            move([pos[0], pos[1] + 1], 2, npd, data, n + 1)
    elif dir == 3:
        if nxt == "-":
            move([pos[0], pos[1] - 1], 4, npd, data, n + 1)
            move([pos[0], pos[1] + 1], 2, npd, data, n + 1)
        elif nxt == "\\":
            move([pos[0], pos[1] + 1], 2, npd, data, n + 1)
        elif nxt == "/":
            move([pos[0], pos[1] - 1], 4, npd, data, n + 1)
        else:
            move([pos[0] + 1, pos[1]], 3, npd, data, n + 1)
    elif dir == 4:
        if nxt == "|":
            move([pos[0] - 1, pos[1]], 1, npd, data, n + 1)
            move([pos[0] + 1, pos[1]], 3, npd, data, n + 1)
        elif nxt == "\\":
            move([pos[0] - 1, pos[1]], 1, npd, data, n + 1)
        elif nxt == "/":
            move([pos[0] + 1, pos[1]], 3, npd, data, n + 1)
        else:
            move([pos[0], pos[1] - 1], 4, npd, data, n + 1)


# print(npd)
# print(npp)
move([0, 0], 2, npd, data, 0)
# print(path)

print("-- Parte A:\t", np.sum(npd > 0))

# %% parte b

energized = []
# move down
for r in range(dims[1]):
    npd = np.zeros(dims, dtype=int)
    move([0, r], 3, npd, data, 0)
    energized.append(np.sum(npd > 0))

# # move up
for r in range(dims[1]):
    npd = np.zeros(dims, dtype=int)
    move([dims[1] - 1, r], 1, npd, data, 0)
    energized.append(np.sum(npd > 0))

# move right
for r in range(dims[0]):
    npd = np.zeros(dims, dtype=int)

    move([r, 0], 2, npd, data, 0)
    energized.append(np.sum(npd > 0))

# move left
for r in range(dims[1]):
    npd = np.zeros(dims, dtype=int)
    move([r, dims[1] - 1], 4, npd, data, 0)
    energized.append(np.sum(npd > 0))

print(energized)
print(max(energized))
