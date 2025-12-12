# %% --- Day 11: Reactor ---
"""
Find all possible paths between YOU and OUT

We have a bunch of nodes connected by the edge list bellow:
a -> b
a -> c
a: b c

The graph structure may be interesting for a recursive function... hm
"""
# %% Data sample 
data_str = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip().split('\n')

# %% Read data from file

with open('day11.txt','r') as f:
    data_str = f.read().strip().split('\n')

# %% Prep data

data = {}
for d in data_str:
    node, child = d.split(':')
    data[node] = child.split()

print(data)

# %% Run the dictionary in a recursive function
def path_to(node, data):
    global liga
    if node=="out":
        return 1
    total_paths = sum(path_to(child, data) for child in data[node])
    return total_paths
    
print("Part 1:", path_to("you", data))