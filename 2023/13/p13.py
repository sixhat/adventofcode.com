import numpy as np

data = open("input.txt").read().strip().split("\n\n")

dimensions_of_patterns = [(len(x.split("\n")), x.find("\n")) for x in data]

data = [
    pat.replace(".", "0 ").replace("#", "1 ").replace("\n", "").strip() for pat in data
]

data = [np.fromstring(x, sep=" ", dtype=int).reshape(dimensions_of_patterns[i]) for i, x in enumerate(data)]


def process_pattern(p, ver=False):
    pat = p.copy()
    if ver:
        pat = pat.transpose()

    num_rows = pat.shape[0]
    potential_mirror = []
    out = []

    for i in range(1, num_rows):
        a = pat[i, :] - pat[i - 1, :]
        # print('a\t',a)
        if not a.any():
            potential_mirror.append(i)

    for el in potential_mirror:
        shorter_side = min(num_rows - el, el)
        brk = False
        for linha in range(shorter_side):
            a = pat[el + linha] - pat[el - linha - 1]
            if a.any():
                brk = True
                break
        if not brk:
            out.append(el)
    return out


total_A = 0
wt = {} # Dictionary for storing outputs (useful for parte_B)

for i, p in enumerate(data):
    hor = process_pattern(p, ver=False)
    ver = process_pattern(p, ver=True)
    h = 0
    v = 0
    if hor:
        total_A += 100 * hor[0]
        h = hor[0]
    if ver:
        total_A += ver[0]
        v = ver[0]

    wt[i] = ([h], [v])

print("-- Parte A:\t", total_A)


def permute_smudge(j, p):
    dim = p.shape
    for row in range(dim[0]):
        for col in range(dim[1]):
            p[row, col] = 1 - p[row, col] # This is the trick of using integers
            a = process_pattern(p, ver=False)
            b = process_pattern(p, ver=True)
            p[row, col] = 1 - p[row, col] # Reverse the swap

            nla = 0
            nlb = 0
            for m in a:
                if m not in wt[j][0]:
                    nla = m
                    return nla*100
            for m in b:
                if m not in wt[j][1]:
                    nlb = m
                    return nlb

total_B = 0
for j, p in enumerate(data):
    total_B+=permute_smudge(j, p)
    
print('-- total B:\t',total_B)
 