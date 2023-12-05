import os
import time
import functools

# input = "demo"
input = "input"

steps = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]
rules = {}


def compara(a, b):
    return b[1] - a[1]


class FromTo:
    def __init__(self, txt: str) -> None:
        txt = txt.split()
        ft = txt[0].split("-")
        self.origin = ft[0]
        self.destination = ft[2]
        i = iter(txt[2::])
        self.t = []
        for a, b, c in zip(i, i, i):
            self.t.append([int(a), int(b), int(c)])
        self.t.sort(key=functools.cmp_to_key(compara))
        print(self.t)

    def calc(self, v: int) -> int:
        o = v
        for r in self.t:
            sh = r[0] - r[1]
            if v < r[1] + r[2] and v >= r[1]:
                o = v + sh
                return o
        return o


def parte_a(data):
    seeds = [int(x) for x in data[0].split()[1::]]
    locations = []
    for seed in seeds:
        val = seed
        for step in steps:
            val = rules[step].calc(val)
        locations.append(val)
    print("-- Total parte A:\t", min(locations))


def parte_b(data):
    min_locations = 999_999_999_999

    seeds = iter([int(x) for x in data[0].split()[1::]])

    tstart = time.time()
    telapsed = 0

    for seed, number in zip(seeds, seeds):
        # print(seed, number)
        max = seed + number
        i = seed
    
        for i in range(seed, seed + number):
            val = passo(i)

            if val < min_locations:
                min_locations = val

            # continue

            if (max - i) % 1_000_000 == 0:
                now = time.time() - tstart
                print("-- ", seed, max, i, max - i, min_locations, now, now - telapsed)
                telapsed = now
                # return
            

    print("-- Total parte B:\t", min_locations)


def passo(val):
    for step in steps:
        val = rules[step].calc(val)
    return val


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n\n")
)
for el in data[1::]:
    ss = FromTo(el)
    rules[ss.origin] = ss


print("---------------")

# parte_a(data)
parte_b(data)
