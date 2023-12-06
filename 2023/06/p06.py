import os

# input = "demo"
input = "input"


def parte_a(data):
    total = 1
    t = [int(x) for x in data[0].split()[1:]]
    d = [int(x) for x in data[1].split()[1:]]
    dp = list(zip(t, d))

    ways_to_beat = []
    for t, d in dp:
        n = 0
        for i in range(t + 1):
            if (t - i) * i > d:
                n += 1
        if n>0:
            ways_to_beat.append(n)
    
    for a in ways_to_beat:
        total = total * a

    print("-- Total parte A:\t", total)


def parte_b(data):
    total = 1
    
    t = [int(data[0].split(":")[1].replace(" ", "").strip())]
    d = [int(data[1].split(":")[1].replace(" ", "").strip())]

    dp = list(zip(t, d))

    ways_to_beat = []
    for t, d in dp:
        n = 0
        for i in range(t + 1):
            if (t - i) * i > d:
                n += 1
        if n>0:
            ways_to_beat.append(n)
    
    for a in ways_to_beat:
        total = total * a
    print("-- Total parte B:\t", total)


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n")
)

parte_a(data)
parte_b(data)
