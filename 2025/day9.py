# %% --- Day 9: Movie Theater ---
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

data = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip().split("\n")

with open("day9.txt") as f:
   data = f.read().strip().split("\n")

data = [Point(*list(map(int,b))) for b in [a.split(",") for a in data]]

print(data)

ma = 0
for i,p in enumerate(data):
    for j in range(i+1, len(data)):
        w = abs(p.x-data[j].x)+1
        h = abs(p.y-data[j].y)+1
        a = w * h
        print(p,data[j], a)
        ma = max(ma, a)
        
print("Parte 1:", ma)


