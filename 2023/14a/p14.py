# %%
# https://adventofcode.com/2023
# https://docs.python.org/3/

from aoc import *

data = open("input.txt", "r").read().strip().splitlines()

aa = rotcw(data)
a = ["#".join(["".join(sorted(x)) for x in di.split("#")]) for di in aa]

a = rotcw(a)
print("-- parte A:", sum([(i + 1) * b.count("O") for i, b in enumerate(a)]))

# Parte B

seen = []
st_cycle = 0
b = data
j = -1
while True:
    j = j+1
    for i in range(4):
        bb = rotcw(b)
        b = ["#".join(["".join(sorted(x)) for x in di.split("#")]) for di in bb]
    if b not in seen:
        seen.append(b)
    else:
        st_cycle = seen.index(b)
        break

    
fp = st_cycle + (1_000_000_000-st_cycle) % (len(seen) - st_cycle)
bb = seen[5]

print("-- parte B:", sum([(len(bb)-i) * b.count("O") for i, b in enumerate(bb)]))

