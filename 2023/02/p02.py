import os
import re

gn = re.compile("Game (\d+)")
rer = re.compile("(\d+) red")
reg = re.compile("(\d+) green")
reb = re.compile("(\d+) blue")


def processa_linha(linha: str) -> tuple[int, int, int, int]:
    game = int(gn.findall(linha)[0])
    red = max([int(x) for x in rer.findall(linha)])
    green = max([int(x) for x in reg.findall(linha)])
    blue = max([int(x) for x in reb.findall(linha)])
    return game, red, green, blue


def parte_a(data: list[str]) -> None:
    total: int = 0
    for linha in data:
        gn, red, green, blue = processa_linha(linha.strip())
        if red <= 12 and green <= 13 and blue <= 14:
            total += gn
    print("-- Total parte A ", total)


def parte_b(data: list[str]) -> None:
    total: int = 0
    for linha in data:
        _, red, green, blue = processa_linha(linha.strip())
        total += red * green * blue
    print("-- Total parte B ", total)


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + "/input", "r")
    .read()
    .strip()
    .split("\n")
)
parte_a(data)
parte_b(data)
