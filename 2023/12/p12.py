# %%
# import os

# https://adventofcode.com/2023/day/12
# https://docs.python.org/3/

input = "demo.txt"

data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n")
)


# %%
def processa_linha(linha):
    print("\n-- process_line", linha)
    _cr = linha.split()
    P = [_cr[0]] # Patterns to test
    nums = [int(x) for x in _cr[1].split(",")]
    print(P, nums)
    
    for n in nums:
        print(n)
        for i, c in enumerate(P):
            print(i, c)

    return 0


pA = 0
# for linha in data:
linha = data[0]
pA += processa_linha(linha)
print("\n-- Parte A:\t", pA)

# %%
