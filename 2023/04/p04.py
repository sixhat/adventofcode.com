import os

# input = "demo"
input = "input"


def processa_linha(linha):
    _l = linha.split(":")
    _l = _l[1]
    w = _l.split("|")
    winning = [int(x) for x in w[0].split()]
    numbers = [int(x) for x in w[1].split()]
    in_winning = []
    for n in numbers:
        if n in winning:
            in_winning.append(n)
    return len(in_winning)


def parte_a(data):
    total = 0
    for linha in data:
        in_winning = processa_linha(linha)
        if in_winning > 0:
            total += 2 ** (in_winning - 1)
    print("Total parte A:\t", total)


def parte_b(data):
    running_ledger = [1 for x in data]
    for i, linha in enumerate(data):
        in_winning = processa_linha(linha)
        for j in range(in_winning):
            running_ledger[i + 1 + j] += running_ledger[i]
    print("Total parte B:\t", sum(running_ledger))


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n")
)

parte_a(data)
parte_b(data)
