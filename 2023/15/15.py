# https://adventofcode.com/2023/day/15 
# https://docs.python.org/3/
# --- Day 15: Lens Library ---

# %% Open Data

data = open("input.txt", "r").read().strip()


# %% Part 1 - Define Hash. 
def hash(s: str) -> int:
    cv = 0
    for ltr in s:
        cv += ord(ltr)
        cv *= 17
        cv %= 256
    return cv


steps = data.split(",")
total = 0
for step in steps:
    total += hash(step)
print("-- Parte A\t", total)

# %% - Part 2 

boxes = [[] for x in range(256)]  # A list of lists
lenses = {}  # a dictionary of lens -> boxes

for step in steps:
    if "=" in step:
        (lens, focal_length) = step.split("=")
        box = hash(lens)
        focal_length = int(focal_length)
        if lens in lenses:
            bb = [a[0] for a in boxes[box]]
            el = bb.index(lens)
            boxes[box][el][1] = focal_length
        else:
            boxes[box].append([lens, focal_length])
            lenses[lens] = box

    if "-" in step:
        lens = step[:-1]
        if lens in lenses:
            box = lenses[lens]
            bb = [a[0] for a in boxes[box]]
            boxes[box].pop(bb.index(lens))
            lenses.pop(lens)

focusing_power = 0
for bi, b in enumerate(boxes):
    if b:
        for li, l in enumerate(b):
            focusing_power += (bi + 1) * (li + 1) * l[1]

print("-- Parte B:\t", focusing_power)
