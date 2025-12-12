# %% --- Day 11: Reactor ---
"""
Find all possible paths between YOU and OUT

We have a bunch of nodes connected by the edge list bellow:
a -> b
a -> c
a: b c

The graph structure may be interesting for a recursive function... hm
"""

# %% Read data from file

with open("day11.txt", "r") as f:
    data_str = f.read().strip().split("\n")

# %% Prep data

data = {}
for d in data_str:
    node, child = d.split(":")
    data[node] = child.split()

print(data)


# %% Run the dictionary in a recursive function
def path_to(node, data):
    if node == "out":
        return 1
    total_paths = sum(path_to(child, data) for child in data[node])
    return total_paths


print("Part 1:", path_to("you", data))

# %% Recursive function again with memoization (without it you'll get stuck forever)


def path_two(node, data, dac, fft, memo: dict = None):
    if memo is None or not isinstance(memo, dict):
        memo = {}

    state_key = (node, dac, fft)

    if state_key in memo:
        return memo[state_key]

    if node == "out":
        if dac and fft:
            memo[state_key] = 1
            return 1
        else:
            memo[state_key] = 0
            return 0

    if node == "dac":
        dac = True
    if node == "fft":
        fft = True

    total_paths = sum(path_two(child, data, dac, fft, memo) for child in data[node])
    memo[state_key] = total_paths
    return total_paths


print("Part 2:", path_two("svr", data, False, False))
