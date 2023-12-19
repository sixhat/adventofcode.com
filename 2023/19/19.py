# %% Load Data
#
# https://adventofcode.com/2023/day/19
# https://docs.python.org/3/
#
# from aoc import *
# import numpy as np
import re

data = open("input.txt", "r").read().strip().split("\n\n")
# print(data)
dims = (len(data), len(data[0]))
# print(dims)

parts = data[1].split("\n")
m = re.compile("\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}")

# print(len(parts))
part = []
for el in parts:
    ob = m.findall(el)
    # print(el, ob)
    obj = {
        "x": int(ob[0][0]),
        "m": int(ob[0][1]),
        "a": int(ob[0][2]),
        "s": int(ob[0][3]),
    }
    # print(obj)
    part.append(obj)

print(part)

rules = [x for x in data[0].splitlines()]
# print(rules)
rule = {}
for r in rules:
    key, a = r[:-1].split('{')
    steps = a.split(',')
    # print(key, steps)
    rule[key] = steps

print(rule)

# %% we have 2 dics rule and part

def process_rule(ru, o):
    print(ru, o)
    for st in ru:
        if ':' in st:
            cond,dst = st.split(':')
            if '<' in cond:
                key,val = cond.split('<')
                if o[key] < int(val):
                    return dst
            if '>' in cond:
                key,val = cond.split('>')
                if o[key] > int(val):
                    return dst
            # print(cond, key, val, dst)
        else: 
            return st
    
A = []
R = []

for p in part:
    r = 'in'
    
    while True:
        r = process_rule(rule[r], p)
        if r=='A':
            A.append(p)
            break
        if r=='R':
            R.append(p)
            break
        

total = [sum(x.values()) for x in A]            
print('-- Parte A:\t', sum(total))
            
