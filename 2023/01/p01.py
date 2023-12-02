import re
import os


def processa_linha(linha: str, nums) -> int:
    dezenas = 10000
    dval = 0
    unidades = -1
    uval = 0

    for num in nums:
        for m in re.finditer(num, linha):
            if m.start() < dezenas:
                dezenas = m.start()
                dval = nums.index(m.group()) % 10
            if m.start() > unidades:
                unidades = m.start()
                uval = nums.index(m.group()) % 10
    return 10 * dval + uval


def parte_B():
    nums = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    inpf = open(os.path.dirname(os.path.realpath(__file__)) + "/input", "r")
    total = 0
    for line in inpf:
        _a = processa_linha(line.strip(), nums)
        total += _a
    print(total)


def parte_A():
    nums = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]
    inpf = open(os.path.dirname(os.path.realpath(__file__)) + "/input", "r")
    total = 0
    for line in inpf:
        _a = processa_linha(line.strip(), nums)
        total += _a
    print(total)

parte_A()
parte_B()