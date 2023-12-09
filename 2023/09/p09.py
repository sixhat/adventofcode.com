import numpy as np

# input = "demo.txt"
input = "input.txt"

data = np.loadtxt(input, dtype=int)

totalA = []
totalB = []
for linha in data:
    ld = []
    sd = []
    ld.append(linha[-1])
    sd.append(linha[0])
    t = linha[:]
    while True:
        t = np.diff(t)
        ld.append(t[-1])
        sd.append(t[0])
        if not t.any():
            break
    sd2 = sd[:]
    for i in range(len(sd) - 2, -1, -1):
        sd2[i] = sd[i] - sd2[i + 1]
    totalA.append(sum(ld))
    totalB.append(sd2[0])
print("-- Total parte A:\t", sum(totalA))
print("-- Total parte B:\t", sum(totalB))
