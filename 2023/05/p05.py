# %% [markdown]
# Day 5 Parte B - Tentar perceber o algoritmo de trabalhar com Ranges.

# %%
import os
import time
import functools

# input = "demo"
input = "input"

steps = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]
rules = {}

data: list[str] = open(f"{input}", "r").read().strip().split("\n\n")


# %%
class FromTo:
    def __init__(self, txt: str) -> None:
        # print("== FromTo =====")
        txt = txt.split()
        ft = txt[0].split("-")
        self.origin = ft[0]
        self.destination = ft[2]
        i = iter(txt[2::])
        self.regras = []
        for a, b, c in zip(i, i, i):
            self.regras.append([int(a), int(b), int(c)])
        # self.regras.sort(key=functools.cmp_to_key(compara))
        # print(self.regras)

    def calc(self, v: int) -> int:
        for r in self.regras:
            sh = r[0] - r[1]
            if r[1] <= v < r[1] + r[2]:
                return v + sh
        return v

    def calc_ranges(self, intervalos: list[tuple[int, int]]) -> list[tuple[int, int]]:
        # print(" calc_ranges\t", intervalos)
        out_intervalos = []

        for regra in self.regras:
            delta = regra[0] - regra[1]
            ir = (regra[1], regra[1] + regra[2])

            novos_intervalos = []
            while intervalos:
                intervalo = intervalos.pop()

                left = (intervalo[0], min(intervalo[1], ir[0]))

                inner = (
                    max(intervalo[0], ir[0]) + delta,
                    min(intervalo[1], ir[1]) + delta,
                )

                right = (max(intervalo[0], ir[1]), intervalo[1])

                if left[1] > left[0]:
                    novos_intervalos.append(left)

                if inner[1] > inner[0]:
                    out_intervalos.append(inner)

                if right[1] > right[0]:
                    novos_intervalos.append(right)

            intervalos = novos_intervalos
        return out_intervalos + intervalos


# %%
for el in data[1::]:
    ss = FromTo(el)
    rules[ss.origin] = ss


# %%
def calc_seeds_1by1(seeds):
    locations = []
    for seed in seeds:
        val = seed
        for step in steps:
            val = rules[step].calc(val)
        locations.append(val)
    return locations


# %%
def parte_a(data):
    seeds = [int(x) for x in data[0].split()[1::]]
    print("-- Total parte A:\t", min(calc_seeds_1by1(seeds)))


# %%
parte_a(data)


# %%
# parte_a(data)
# parte_b(data)
min_locations = 999_999_999_999

# need ranges here [a,b) (b is exclusive)
a_seeds = [int(x) for x in data[0].split()[1::]]
b_seeds = list(zip(a_seeds[::2], a_seeds[1::2]))
ranges = [(a[0], a[0] + a[1]) for a in b_seeds]

# print("---\t", ranges)
# ranges = [(90, 110)]
P2 = []
ran = ranges
for ran in ranges:
    intervalos = [ran]
    # print(r)
    for step in steps:
        # print("-- step\t", step)
        intervalos = rules[step].calc_ranges(intervalos)
        # print("OUT ranges\t", R)
    P2.append(min(intervalos)[0])
print("-- Total parte B:\t", min(P2))
