edges = [sorted(line.strip().split("-")) for line in open(0).readlines()]

nodes = set()
for e in edges:
    nodes.add(e[0])
    nodes.add(e[1])

sol = set()

for e in edges:
    for v in nodes:
        if v[0]=='t':
            a = sorted([e[0], v])
            b = sorted([e[1], v])
            if a in edges and b in edges :
                sol.add(",".join(sorted([e[0], e[1], v])))

print("\n".join(sol))
print(len(sol))
