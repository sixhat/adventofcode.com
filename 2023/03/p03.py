import os
import re

red = re.compile("(\d+)")
ren = re.compile("[^.\d]+")
restar = re.compile("\*{1}")


def dim(data: list[str]) -> dict[str, int]:
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
    if nsv is not None:
        return val
    else:
        return 0


def find_numbers(data: list[str]) -> list[tuple[int, int, int]]:
    d = dim(data)
    numbers = []
    for y in range(d["y"]):
        matches = red.finditer(data[y])
        for m in matches:
            numbers.append((y, m.start(), m.end()))
    return numbers


def find_gears(data: list[str]) -> list[tuple[int, int, int]]:
    d = dim(data)
    stars = []
    for y in range(d["y"]):
        matches = restar.finditer(data[y])
        for m in matches:
            stars.append((y, m.start(), m.end()))
    return stars


def parte_a(data: list[str]) -> None:
    # Find numbers and their indicies (can be done with regex)
    d = dim(data)
    total: int = 0
    for y in range(d["y"]):
        matches = red.finditer(data[y])
        for m in matches:
            total += check_match(m, y)
    print("-- Total parte A:\t", total)


def check_gear(star: tuple[int, int, int], nums: list[tuple[int, int, int]]):
    spokes = []
    for n in nums:
        if abs(star[0] - n[0]) > 1:
            continue
        if (
            star[1] - n[2] == 0
            or n[1] - star[1] == 1
            or (star[1] >= n[1] and n[2] >= star[1])
        ):
            spokes.append(n)
    if len(spokes) == 2:
        return spokes
    else:
        return None


def parte_b(data: list[str]) -> None:
    all_numbers = find_numbers(data)
    all_gears = find_gears(data)
    total_gear_ratios = 0
    for star in all_gears:
        spokes = check_gear(star, all_numbers)
        if spokes is not None:
            spoke0 = int(data[spokes[0][0]][spokes[0][1] : spokes[0][2]])
            spoke1 = int(data[spokes[1][0]][spokes[1][1] : spokes[1][2]])
            total_gear_ratios += spoke0 * spoke1
    print("-- Total parte B\t", total_gear_ratios)


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + "/input", "r")
    .read()
    .strip()
    .split("\n")
)
parte_a(data)
parte_b(data)
