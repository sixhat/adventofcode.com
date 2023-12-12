# %%
# Load data and libraries
import numpy as np

# input = "demo2.txt"
input = "input.txt"

data = open(f"{input}", "r").read().strip().split("\n")
data[:] = [list(e) for e in data]
tamanho = (len(data), len(data[0]))

# %%
# Set dictionaries for navigation
dic = {
    "F": [(0, 1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "7": [(0, -1), (1, 0)],
}

# 0 up 1 down 2 left 3 right
dirs = np.array([(-1, 0), (1, 0), (0, -1), (0, 1)])

# %%
# Find starting position of S
def find_s():
    for y, linha in enumerate(data):
        for x, elemento in enumerate(linha):
            if elemento == "S":
                return (y, x)
                break


start_pos = np.array(find_s())
# print(start_pos)

# %%
# find possible directions for S
can_go = []
for e, dir in enumerate(dirs):
    _p = start_pos + dir
    el = data[_p[0]][_p[1]]
    # print(e,el)

    if e == 0 and el in "7|F":
        can_go.append(e)
    if e == 1 and el in "L|J":
        can_go.append(e)
    if e == 2 and el in "-LF":
        can_go.append(e)
    if e == 3 and el in "-J7":
        can_go.append(e)

# print(can_go)

# %%
# part A
m = -np.ones(tamanho, dtype=np.int16)
m[*start_pos] = 0
pA = start_pos
pB = start_pos
cA = start_pos + dirs[can_go[0]]
cB = start_pos + dirs[can_go[1]]
pathA = [start_pos]
pathB = [start_pos]

while True:
    m[*cA] = m[*pA] + 1
    m[*cB] = m[*pB] + 1
    pA = cA
    pB = cB

    pathA.append(cA)
    pathB.append(cB)

    mA = dic[data[cA[0]][cA[1]]]
    mB = dic[data[cB[0]][cB[1]]]

    tmA = cA + mA[0]
    cA = cA + mA[0] if m[*tmA] == -1 else cA + mA[1]
    tmB = cB + mB[0]
    cB = cB + mB[0] if m[*tmB] == -1 else cB + mB[1]

    
    if m[*cA] != -1:
        break
# print(m)

np.savetxt("out.txt", m, fmt="%d")
# print(m[*cA], m[*cB])
print("-- Part A:\t", m[*cA] + 1)

# %%
# part B (make a full path, mark lefts or right, diffusion)
rpathB=list(reversed(pathB))
full_path = pathA[:-1] + rpathB

# %%
## mark lefts 
for i in range(1,len(full_path)):
    o = full_path[i-1]
    d = full_path[i]
    # m[*d] = i-1
    v = d-o
    # print(o,d,v)
    if (v==np.array([-1, 0])).all():
        try:
            # print(o)
            oo = o + (0,-1)
            do = d + (0,-1)
            if m[*oo] == -1:
                m[*oo] = -2
            if m[*do] == -1:
                m[*do] = -2
        except:
            pass
    if (v==np.array([1, 0])).all():
        try:
            # print(o)
            oo = o + (0,1)
            do = d + (0,1)
            if m[*oo] == -1:
                m[*oo] = -2
            if m[*do] == -1:
                m[*do] = -2
        except:
            pass
    if (v==np.array([0, 1])).all():
        try:
            # print(o)
            oo = o + (-1,0)
            do = d + (-1,0)
            if m[*oo] == -1:
                m[*oo] = -2
            if m[*do] == -1:
                m[*do] = -2
        except:
            pass
    if (v==np.array([0, -1])).all():
        try:
            # print(o)
            oo = o + (1,0)
            do = d + (1,0)
            if m[*oo] == -1:
                m[*oo] = -2
            if m[*do] == -1:
                m[*do] = -2
        except:
            pass
# print(m)


np.savetxt("out2.txt", m, fmt="%d")


# %%
# Difuse -2 

def difuse(pos):
    for d in [(-1,0), (1,0), (0,-1), (0,1)]:
        try:
            oo = pos +d
            if m[*oo] == -1:
                m[*oo] = -2
        except:
            # print("H", oo)
            pass


# %%
m2 = np.where(m==-2)
q2 = len(m2[0])

for ll in range(10):
    for i,v in enumerate(m2[0]):
        p = np.array((v, m2[1][i]))
        # p = np.array((m2[0][0], m2[1][0]))
        # print(p)
        difuse(p)
    m2 = np.where(m==-2)
    q3 = len(m2[0])

print("-- Parte B:\t", np.sum(m==-2))
np.savetxt("out3.txt", m, fmt="%d")    


# %%



