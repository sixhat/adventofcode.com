# %%
# https://adventofcode.com/2023
# https://docs.python.org/3/

from aoc import pprint
import numpy as np

data = open("demo.txt", "r").read().strip().splitlines()
pprint(data)
dims = (len(data), len(data[0]))
print(dims)
npd = np.zeros(dims, dtype=int)


def valor(row, col):
    global data
    return int(data[row][col])


for row in range(dims[0]):
    for col in range(dims[1]):
        npd[row, col] = valor(row, col)
print(npd)

# %% Parte A - Is it a BFS? Maybe with some small changes
visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    graph[node] = 1  # v(*node)
    nstep = 0

    while queue:
        m = queue.pop(0)

        neighbours = []

        nei2 = [
            (m[0] - 1, m[1]),
            (m[0] + 1, m[1]),
            (m[0], m[1] - 1),
            (m[0], m[1] + 1),
        ]
        for neighbour in nei2:
            if (
                neighbour[0] < 0
                or neighbour[1] < 0
                or neighbour[0] == dims[0]
                or neighbour[1] == dims[1]
            ):
                continue
            if neighbour not in visited:
                neighbours.append(neighbour)

        print(m, "-> to_visit ->", neighbours)
        print(graph)
        dist = [valor(*d) for d in neighbours]
        for i, nei in enumerate(neighbours):
            mind = min(dist)
            if nei not in visited and dist[i] == mind:
                graph[nei] = graph[m] + 1  # v(*nei)
                dir = (m[0] - nei[0], m[1] - nei[1])
                print("--dir ", nei, dir)

                add = True
                last3 = []
                for n in range(4):
                    ndr = nei[0] + dir[0] * n
                    ndc = nei[1] + dir[1] * n
                    if ndr < 0 or ndr == dims[0] or ndc < 0 or ndc == dims[1]:
                        break
                    print((ndr, ndc), graph[ndr, ndc])
                    last3.append(graph[ndr, ndc])

                print("--- Last 3", last3)
                if len(last3) == 4:
                    if last3[-1] - last3[0] == 3:
                        add = False
                if add:
                    print("-- Nei", nei)
                    visited.append(nei)
                    queue.append(nei)
                    if nei == (dims[0] - 1, dims[1] - 1):
                        return

        # break


# %% dijkstra's
def find_neighbours(graph, node):
    neighbours = []

    nei2 = [
        (node[0] - 1, node[1]),
        (node[0] + 1, node[1]),
        (node[0], node[1] - 1),
        (node[0], node[1] + 1),
    ]
    for neighbour in nei2:
        if (
            neighbour[0] < 0
            or neighbour[1] < 0
            or neighbour[0] == graph.shape[0]
            or neighbour[1] == graph.shape[1]
        ):
            continue
        neighbours.append(neighbour)
    return neighbours


def linha(u, v, pre):
    p = [v, u]
    if len(pre) < 4:
        return 0

    for a in range(3):
        p.append(pre[p[-1][0]][p[-1][1]])

    dr = max(p[:][0]) - min(p[:][0])
    dc = max(p[:][1]) - min(p[:][1])
    return max(dr, dc)


# def dijkstra(graph, node):
#     dist = np.zeros(graph.shape, dtype=int)
#     prev = [
#         [(-1, -1) for col in range(graph.shape[1])] for row in range(graph.shape[0])
#     ]
#     Q = []
#     for row in range(graph.shape[0]):
#         for col in range(graph.shape[1]):
#             dist[(row, col)] = 1000
#             Q.append((row, col))
#     dist[0, 0] = graph[0, 0]

#     while Q:
#         els = [dist[el] for el in Q]
#         imin = els.index(min(els))
#         u = Q[imin]
#         Q.remove(u)

#         nei = find_neighbours(graph, u)
#         pnei = []
#         for e in nei:
#             if linha(u, e, prev) < 4:
#                 pnei.append(e)

#         for v in pnei:
#             if v in Q:
#                 alt = dist[u] + (graph[v])
#                 if alt < dist[v]:
#                     dist[v] = alt
#                     prev[v[0]][v[1]] = u
#     print(dist)
#     print(prev)
#     return prev


# prevs = dijkstra(npd, (0, 0))
# path = []
# el = (len(prevs) - 1, len(prevs[0]) - 1)
# p = np.zeros(npd.shape, dtype=int)
# while el != (0, 0):
#     path.append(el)
#     el = prevs[el[0]][el[1]]
#     p[el] = 1
# # print(path, npd)
# print(p)
# p[-1, -1] = 1
# print(p * npd)
# print(np.sum(p * npd))

# %% push pop backtracking algorithm

print(npd)

def find_neighbours(graph, node):
    neighbours = []

    nei2 = [
        (node[0] - 1, node[1]),
        (node[0] + 1, node[1]),
        (node[0], node[1] - 1),
        (node[0], node[1] + 1),
    ]
    for neighbour in nei2:
        if (
            neighbour[0] < 0
            or neighbour[1] < 0
            or neighbour[0] == graph.shape[0]
            or neighbour[1] == graph.shape[1]
        ):
            continue
        neighbours.append(neighbour)
    return(neighbours)

sols = []
def maze(g, c):
    if c[-1]!=g.shape:
        return False
    else:
        sols.append(c)
        return True
    nei = find_neighbours(g, c[-1])
    return maze(g, c)

path = [(0,0)]

maze(npd, path)
