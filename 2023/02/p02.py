import os
import re
# https://adventofcode.com/2023/day/2


def processa_linha(linha, r, g, b):
    # regex -find game number return games numbers possible <=r,g,b
    gn = re.compile("Game (\d+)")
    rer = re.compile("(\d+) red")
    reg = re.compile("(\d+) green")
    reb = re.compile("(\d+) blue")
    
    game = int(gn.findall(linha)[0])
    red = max([int(x) for x in rer.findall(linha)])
    green = max([int(x) for x in reg.findall(linha)])
    blue = max([int(x) for x in reb.findall(linha)])
    
    if red <= r and green <= g and blue <= b:
        return game
    else:
        return 0

def parte_a(data):
    total = 0
    for linha in data:
        total += processa_linha(linha.strip(), 12, 13, 14)
    print ("-- Total parte A ", total)

def parte_b(data):
    for linha in data:
        processa_linha(linha.strip(), 12, 13, 14)


inpf = open(os.path.dirname(os.path.realpath(__file__)) + "/input", "r")
parte_a(inpf)
# parte_b(inpf)
