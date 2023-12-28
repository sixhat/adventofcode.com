import re


def run(lin, ns):
    any = re.compile("|".join(ns))
    els = any.findall(lin)
    return 10 * (ns.index(els[0]) % 10) + (ns.index(els[-1]) % 10)


data = open("input", "r").read().strip().split("\n")
partA = [str(x) for x in range(10)]
partB = partA + [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

print("Part 1:\t", sum([run(d, partA) for d in data]))
print("Part 2:\t", sum([run(d, partB) for d in data]))
