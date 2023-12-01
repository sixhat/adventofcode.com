import re


def processa_linha(linha: str)-> int:
    dezenas = 10000
    dval = 0
    unidades = -1
    uval = 0
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

    for num in nums:
        for m in re.finditer(num, linha):
            if m.start() < dezenas:
                print("dez")
                dezenas = m.start()
                dval = nums.index(m.group()) % 10
            if m.start() > unidades:
                print("uni")
                unidades = m.start()
                uval = nums.index(m.group()) % 10
            print(m.start(), m.end(), m.group(), unidades, dezenas, dval, uval)
    return 10 * dval + uval


inpf = open("input", "r")

total = 0
for line in inpf:
    print(line.strip())
    _a = processa_linha(line.strip())
    total += _a
    print(_a, total)
