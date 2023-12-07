import os

# https://adventofcode.com/2023
# https://docs.python.org/3/

input = "demo"
# input = "input"


def parte_a(data):
    total = 0
    print("-- Total parte A:\t", total)


def parte_b(data):
    total = 0
    print("-- Total parte B:\t", total)


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n")
)

print(data)

parte_a(data)
parte_b(data)
