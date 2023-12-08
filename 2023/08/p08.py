import os
import re
import math
## https://adventofcode.com/2023
## https://docs.python.org/3/

# input = "demo"
input = "input"


## Read DATA ########################################################
data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n")
)

## Setup Data ########################################################
LR = data[0]
step: dict[str, tuple[str, str]] = {}
res = re.compile("([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")
for linha in data[2:]:
    r = res.findall(linha)
    step[r[0][0]] = (r[0][1], r[0][2])
L = len(LR)

## PART A ########################################################
pos = "AAA"
i = 0
num_steps = 0
while pos != "ZZZ":
    pos = step[pos][0] if (LR[i] == "L") else step[pos][1]
    i = (i + 1) % L
    num_steps += 1
print("-- Total parte A:\t", num_steps)

## PART B ########################################################
def run_to_z(pos, stp):
    while True:
        i = stp % L
        d = 0 if (LR[i] == "L") else 1
        pos = step[pos][d]
        stp += 1
        if pos[2] == "Z":
            break
    return pos, stp

a_pos: list[str] = []
for p in step.keys():
    if p[2] == "A":
        a_pos.append(p)

i_pos = [0 for x in a_pos]
# Calculate the shortest paths for each ??A -> ??Z
for a, _ in enumerate(i_pos):
    a_pos[a], i_pos[a] = run_to_z(a_pos[a], i_pos[a])
# Calculate the Least Common Multiple of all values
part_b = math.lcm(*i_pos)
print("-- Total parte B:\t", part_b)
