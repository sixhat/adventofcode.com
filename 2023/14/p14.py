# https://adventofcode.com/2023
# https://docs.python.org/3/

import aoc

data = open("demo.txt", "r").read().strip().splitlines()

data[:] = [list(a) for a in data]
# print(data)

# double pointer from the end with swap in place iif b not #
# roll O north, then calc load.
cache = {}


# @profile
def roll(str_list):
    st = str_list[:]

    if tuple(st) in cache.keys():
        return cache[tuple(st)]

    out = roll_to_end("O", ".", "#", str_list)
    # out = rollb(st)

    cache[tuple(st)] = out
    return out


# @profile
def rollb(str_list):
    st = str_list[:]
    o_pos = []
    for i, e in enumerate(st):
        if e in "O":
            o_pos.append(i)
        if o_pos:
            if e in "#":
                k = i - 1
                while o_pos:
                    el = o_pos.pop()
                    st[el] = "."
                    st[k] = "O"
                    k -= 1
            if i == len(st) - 1:
                k = i
                while o_pos:
                    el = o_pos.pop()
                    st[el] = "."
                    st[k] = "O"
                    k -= 1
    return st


# @profile
def roll_to_end(char, empty, stop, str_list):
    st = str_list[:]
    ls = len(st)
    for i in range(ls):
        # Mark first Char
        if st[i] == char:
            p = i
            for j in range(i, ls):
                if st[j] == empty:
                    p = j
                if st[j] == stop or j == ls - 1:
                    st[i] = empty
                    st[p] = char
                    break
    return st


dir_north = [list(a) for a in zip(*data)]
dir_north[:] = [a[::-1] for a in dir_north]

# print(dir_north)

totalA = 0
for el in dir_north:
    # val = rollb(el)
    val = roll(el)
    for i, c in enumerate(val):
        totalA += (i + 1) if c == "O" else 0

print("-- Total parte A:\t", totalA)

totalB = 0


# 1_000_000_000
# @profile

ct = {}
lt = []
nh =0

def f2(dat, i):
    global  nh
    global lt

    key = "".join(["".join(e) for e in dat])
    if key in ct:
        nh = lt.index(key)
        return ct[key]
    
    
    # Roll North
    dir_north = [list(a) for a in zip(*dat)]
    dir_north[:] = [a[::-1] for a in dir_north]
    for i, el in enumerate(dir_north):
        dir_north[i] = roll(el)

    # Roll West
    dir_west = [list(a) for a in zip(*dir_north)]
    dir_west[:] = [a[::-1] for a in dir_west]
    for i, el in enumerate(dir_west):
        dir_west[i] = roll(el)

    # Roll South
    dir_south = [list(a) for a in zip(*dir_west)]
    dir_south[:] = [a[::-1] for a in dir_south]
    for i, el in enumerate(dir_south):
        dir_south[i] = roll(el)

    # Roll East
    dir_east = [list(a) for a in zip(*dir_south)]
    dir_east[:] = [a[::-1] for a in dir_east]
    for i, el in enumerate(dir_east):
        dir_east[i] = roll(el)
    
    lt.append(key)
    ct[key] = dir_east
    return(dir_east)

def f():
    global data
    dir_east = data.copy()

    for n in range(1_4):
        dir_east = f2(dir_east, n)
        if nh > 0:
            print(n, nh)
            pf = nh + (1_000_000_000 - nh) % (n-nh)
            print(pf)
            # print(ct)
            totalB = 0
            
            key = lt[pf]
            val = ct[key]
            print(val)
            for i, c in enumerate(val):
                totalB += (i + 1) if c == "O" else 0
            print(totalB)
            break
    
    

f()
