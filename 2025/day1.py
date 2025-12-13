with open(0, "r") as f:
    data = f.read().strip().split("\n")

data = [int(a[1:]) if a[0] == "R" else -int(a[1:]) for a in data]
tot = 0
tot2 = 0
start = 50
for e in data:
    nt = abs(e) // 100
    rt = e - nt * 100 if e >= 0 else e + nt * 100
    tot2 += nt + 1 if start + rt > 99 or (start + rt <= 0 and start != 0) else nt

    ns = start + e
    start = ns % 100
    tot += 1 if start == 0 else 0

print("Part 1:", tot)
print("Part 2:", tot2)
