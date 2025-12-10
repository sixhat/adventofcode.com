from pathlib import Path
from dataclasses import dataclass
from typing import List

"""
What do you get when the Travelling Salesman Problem doesn't have
enough roads to visit every city? Donkey mail?
Well this is a MST finding algorithm by
Kruskal (https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

function Kruskal(Graph G) is
    F:= ∅
    for each v in G.Vertices do
        MAKE-SET(v)

    for each {u, v} in G.Edges ordered by increasing weight({u, v}) do
        if FIND-SET(u) ≠ FIND-SET(v) then
            F := F ∪ { {u, v} }
            UNION(FIND-SET(u), FIND-SET(v))
    return F
"""


@dataclass(frozen=True)
class Junction:
    x: int
    y: int
    z: int


@dataclass
class Edge:
    distance_sq: int
    nodes: List[Junction]

    # Could have used (order=True in the dataclass, but this makes it twice faster)
    def __lt__(self, other):
        return self.distance_sq < other.distance_sq


def dist_sq(a: Junction, b: Junction) -> int:
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2


def day8_data(fich):
    txt = Path(fich).read_text().strip().splitlines()
    data = [Junction(*map(int, line.split(","))) for line in txt]
    return data


def calc_edges(junctions: List[Junction]) -> List[Edge]:
    edges = []
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            d = dist_sq(junctions[i], junctions[j])
            e = Edge(d, [junctions[i], junctions[j]])
            edges.append(e)

    return sorted(edges)


def day8_solve_kruskal(junctions, part=-1):
    """
    function Kruskal(Graph G) is
    F:= ∅
    for each v in G.Vertices do
        MAKE-SET(v)

    for each {u, v} in G.Edges ordered by increasing weight({u, v}) do
        if FIND-SET(u) ≠ FIND-SET(v) then
            F := F ∪ { {u, v} }
            UNION(FIND-SET(u), FIND-SET(v))
    return F

    > This implementation is not fast, as it should 
    > have a DSU (Disjoint Set Union) implementation to make it faster
    """
    edges = calc_edges(junctions)
    if part == 1:
        edges = edges[:1000]
    F = [[j] for j in junctions]
    for k, e in enumerate(edges):
        a, b = e.nodes
        ia = -1
        ib = -1
        for i in range(len(F)):
            f = F[i]
            if a in f:
                ia = i
            if b in f:
                ib = i
            if ib > -1 and ia > -1:
                break
        if ia != ib and ia > -1 and ib > -1:
            nl = list(set(F[ia]).union(set(F[ib])))
            F.append(nl)
            F.pop(max(ia, ib))
            F.pop(min(ia, ib))
        if len(F) == 1:
            return e.nodes[0].x * e.nodes[1].x
    nn = sorted([len(x) for x in F], reverse=True)
    return nn[0] * nn[1] * nn[2]


data = day8_data("day8.txt")
print("Parte 1:", day8_solve_kruskal(data, 1))
print("Parte 2:", day8_solve_kruskal(data))
