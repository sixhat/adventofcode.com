# %%
# Load data and libraries
import numpy as np

# input = "demo.txt"
input = "input.txt"

fulltxt = open(f"{input}", "r").read().strip()
universe = fulltxt.split("\n")
universe[:] = [list(e) for e in universe]

universe_size = (len(universe), len(universe[0]))

expansion_factors = [2, 1_000_000]
## partA - Compute Minkowski distances order 1 (cityblock) (https://en.wikipedia.org/wiki/Minkowski_distance) with expansion_factor = 2
## partB - repeat with expansion_factor = 1_000_000


# %%
## Create numpy array and index empty rows,cols
nd = fulltxt.replace(".", "0 ").replace("#", "1 ").replace("\n", "").strip()
universe = np.fromstring(nd, sep=" ").reshape(universe_size)

empty_rows = np.sum(universe, axis=(1))
empty_cols = np.sum(universe, axis=(0))

indx_row = [x[0] for x in np.argwhere(empty_rows == 0)]
indx_col = [x[0] for x in np.argwhere(empty_cols == 0)]


# %%
## Get galaxies (1s) positions
galaxies = np.argwhere(universe == 1).tolist()


# %%
## Calculate Cityblock distance
from scipy.spatial.distance import pdist, squareform


# %%
## For existing distances compute extra distance due to expansion
## order is (row,col)
for expansion_factor in expansion_factors:
    dists = squareform(pdist(galaxies, metric="cityblock"))
    ## calc lower triangle of distances
    dists = dists * np.tri(dists.shape[0], dists.shape[1])
    for row in range(len(galaxies)):
        for col in range(row):
            a = galaxies[col]
            b = galaxies[row]

            delta1 = abs(a[0] - b[0])
            delta2 = abs(a[1] - b[1])

            ct_row = 0
            mia = min(a[0], b[0])
            mxa = max(a[0], b[0])
            for c in indx_row:
                if mia < c < mxa:
                    ct_row += 1

            ct_col = 0
            mia = min(a[1], b[1])
            mxa = max(a[1], b[1])
            for c in indx_col:
                if mia < c < mxa:
                    ct_col += 1

            dists[row, col] = (
                dists[row, col]
                + (ct_row * expansion_factor - ct_row)
                + (ct_col * expansion_factor - ct_col)
            )
    print(int(sum(sum(dists))))
