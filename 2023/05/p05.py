import os

# input = "demo"
input = "input"


class FroTo:
    def __init__(self, txt: str) -> None:
        txt = txt.split()
        ft = txt[0].split("-")
        self.origin = ft[0]
        self.destination = ft[2]
        i = iter(txt[2::])
        self.t = []
        for a, b, c in zip(i, i, i):
            self.t.append((int(a), int(b), int(c)))

    def calc(self, v: int):
        o = v
        for r in self.t:
            if v - r[1] >= 0 and v - r[1] - r[2] < 0:
                o = r[0] + v - r[1]
        return o


def parte_a(data):
    total = 0
    seeds = [int(x) for x in data[0].split()[1::]]
    rules = {}
    for el in data[1::]:
        ss = FroTo(el)
        rules[ss.origin] = ss
    # print(rules)
    steps = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]
    locations = []
    for seed in seeds:
        val = seed
        for step in steps:
            val = rules[step].calc(val)
        locations.append(val)
        print(seed, val) 
    print(min(locations), locations) 
    print("-- Total parte A:\t", total)


def parte_b(data):
    total = 0
    print("-- Total parte B:\t", total)


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n\n")
)

print("---------------")

parte_a(data)
parte_b(data)
