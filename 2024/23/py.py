edges = [sorted(line.strip().split("-")) for line in open(0).readlines()]

edg = set()
for e in edges:
    edg.add(e[0])
    edg.add(e[1])

sol = set()

for e in edges:
    for v in edg:
        a = sorted([e[0], v])
        b = sorted([e[1], v])
        if v[0]=='t' and a in edges and b in edges :
            sol.add(",".join(sorted([e[0], e[1], v])))

print("\n".join(sol))
print(len(sol))
