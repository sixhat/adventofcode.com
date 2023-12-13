# %%
# import os
import re
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
def check(linha, n, grupo):
    print(linha, n, grupo)
    out = 0
    ## Base Case
    if n >= len(grupo) and len(linha) > 0:
        return 0
    if n >= len(grupo) - 1 and len(linha) == 0:
        return 1
    ## Recursion
    print("linha", linha, n)
    if linha[0] == "#":
        b = grupo[n]
        print("a", b, linha)
        try:
            t = linha[0:b]
        except:
            print("ERRR", type(b))
        if "." not in t:
            out += check(linha[b:], n + 1, grupo)
    if linha[0] == "?":
        print("b")
        out += check("." + linha[1:], n, grupo)
        out += check("#" + linha[1:], n, grupo)
    if linha[0] == ".":
        print("c")
        out += check(linha[1:], n, grupo)
    return out


pA = 0

# for linha in data:
linha, nums = data[0].split(" ")
nums = [int(x) for x in nums.split(",")]
print(linha, nums)
n = 0
pA += check(linha, n, nums)

print("\n-- Parte A:\t", pA)

# %%

