import os
import re
from typing import List

red = re.compile("(\d+)")
ren = re.compile("[^.\d]+")


def dim(data):
    "Returns xdim, ydim"
    return {"x": len(data[0]), "y": len(data)}


def check_match(m: re.Match, y: int) -> int:
    "Returns 0 or the value of match"
    d = dim(data)
    val = int(m.group())
    xs = max(m.start() - 1, 0)
    ys = max(y - 1, 0)
    xe = min(m.end() + 1, d["x"])
    ye = min(y + 2, d["y"])
    ns = ""
    for i in range(ys, ye):
        ns += data[i][xs:xe].strip()
    nsv = ren.search(ns)
    if nsv != None:
        return val
    else:
        return 0


def parte_a(data):
    # Find numbers and their indicies (can be done with regex)
    d = dim(data)
    total = 0
    for y in range(d["y"]):
        matches = red.finditer(data[y])
        for m in matches:
            # print(m)
            total += check_match(m, y)
    print("-- Total parte A:\t", total)


def parte_b(data):
    pass


inpf = open(os.path.dirname(os.path.realpath(__file__)) + "/input", "r")
data: List[str] = inpf.readlines()
inpf.close()

parte_a(data)
parte_b(data)
