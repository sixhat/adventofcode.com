# %% --- Day 8: Playground ---
from pathlib import Path
from dataclasses import dataclass, field
from typing import List
"""
What do you get when the Travelling Salesman Problem doesn't have
enough roads to visit every city? Donkey mail?
"""

@dataclass(order=True, frozen=True)
class Junction:
    x: int
    y: int
    z: int

@dataclass(order=True)
class Edge:
    distance_sq: int
    nodes: List[Junction]

def dist_sq(a: Junction, b: Junction) -> int:
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2

def print_distances(edges: List[Edge]):
    for e in edges:
        print(e)

def day8_data():
    txt = Path("day8.txt").read_text().strip().splitlines()
    data = [Junction(*map(int, a)) for a in [line.split(",") for line in txt]]
    return data

def calc_edges(junctions: List) -> Edge:
    edges = []
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            d = dist_sq(junctions[i], junctions[j])
            e = Edge(d, [junctions[i], junctions[j]])
            edges.append(e)
    return sorted(edges)

def merge_components(a: List, b: List) -> List:
    return list(set(b).union(set(a)))

def in_graph(a, g):
    for c in g:
        if a in c:
            return c
    return False

def day8_solve_1(junctions):
    edges = calc_edges(junctions)
    set_edges = [set(e.nodes) for e in edges[:1000]]
    t = 0
    while t != -1:
        t = 0
        ns = []
        rm = []
        # print(set_edges)
        for i, a in enumerate(set_edges):
            for j in range(i + 1, len(set_edges)):
                b = set_edges[j]
                if a.intersection(b):
                    t += 1
                    if a not in rm:
                        rm.append(a)
                    if b not in rm:
                        rm.append(b)
                    u = a.union(b)
                    if u not in ns: 
                        ns.append(u)
                    break
                    
        # print("\n\n\n", t)
        # print("RM",rm)
        # print("NS",ns)
        # print("-----")
        for r in rm:
            # print(r)
            if r in set_edges:
                set_edges.remove(r)
        set_edges.extend(ns)

        if t == 0:
            break   


    m = sorted([len(el) for el in set_edges], reverse=True)
    print(m[0]*m[1]*m[2])        
    

data = day8_data()
# print((data))
day8_solve_1(data)
# %%
