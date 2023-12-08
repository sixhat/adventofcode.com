import os

# input = "demo"
input = "input"


def parte_a(data):
    total = 1
    t = [int(x) for x in data[0].split()[1:]]
    d = [int(x) for x in data[1].split()[1:]]
    dp = list(zip(t, d))

    for t, d in dp:
        n = [(t - i) * i > d for i in range(t + 1)].count(True)
        if n > 0:
            total = total * n

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

parte_a(data)
parte_b(data)
