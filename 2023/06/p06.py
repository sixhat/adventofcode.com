import os
import time

# input = "demo"
input = "input"

start = 0


def tic():
    global start
    start = time.time()


def toc():
    print(time.time() - start)


def parte_a(data):
    total = 1
    t = [int(x) for x in data[0].split()[1:]]
    d = [int(x) for x in data[1].split()[1:]]
    dp = list(zip(t, d))

    ways_to_beat: list[int] = []
    for t, d in dp:
        n = 0
        for i in range(t + 1):
            if (t - i) * i > d:
                n += 1
        if n > 0:
            ways_to_beat.append(n)

    for a in ways_to_beat:
        total = total * a

    print("-- Total parte A:\t", total)


def parte_b(data: list[str]):
    t: int = int(data[0].split(":")[1].replace(" ", "").strip())
    d: int = int(data[1].split(":")[1].replace(" ", "").strip())
    
    total = [(t - i) * i > d for i in range(t + 1)].count(True)
    print("-- Total parte B:\t", total)


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n")
)

# parte_a(data)
tic()
parte_b(data)
toc()
