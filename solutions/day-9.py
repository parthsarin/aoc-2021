"""
File: day-9.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *
from itertools import product
from functools import reduce
from operator import mul

DAY = 9
YEAR = 2021
data = get_input(write=True, day=DAY, year=YEAR)

# --- Part 1 ---
data = data.split('\n')
data = [list(map(int, list(x))) for x in data]
num_rows = len(data)
num_cols = len(data[0])

def get_neighbors(i, j):
    potential_neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    neighbors = [
        (i, j)
        for i, j in potential_neighbors
        if 0 <= i < num_rows and 0 <= j < num_cols
    ]

    neighbor_val = [data[i][j] for i, j in neighbors]

    return neighbors, neighbor_val

low_points = [
    (i, j)
    for i, j in product(range(num_rows), range(num_cols))
    if all(data[i][j] < x for x in get_neighbors(i, j)[1])
]

ans_1 = sum(data[i][j] + 1 for i, j in low_points)

# --- Part 2 ---
def basin_at(i, j):
    if (i, j) not in low_points:
        raise ValueError('Not a low point')
    
    basin_points = set()
    q = [(i, j)]
    while q:
        point = q.pop()
        basin_points.add(point)

        pi, pj = point
        for neighbor, n_val in zip(*get_neighbors(*point)):
            if neighbor in basin_points:
                continue

            # are we moving upwards?
            moving_up = n_val > data[pi][pj]
            reached_max = n_val == 9
            if moving_up and not reached_max:
                q.append(neighbor)
    
    return basin_points

basin_sizes = [len(basin_at(*point)) for point in low_points]
basin_sizes = sorted(basin_sizes, reverse=True)
ans_2 = reduce(mul, basin_sizes[:3])

# --- Submission Code ---
if not os.path.exists(f'../puzzles/day-{DAY}.md'):
    # Level 2 hasn't been generated yet; we're on level 1
    correct = submit(ans_1, level=1, day=DAY, year=YEAR)
    if correct:
        puzzle = get_puzzle(day=DAY, year=YEAR)
        with open(f'../puzzles/day-{DAY}.md', 'w') as f:
            f.write(puzzle)
else:
    # Level 2 has been generated; we're on level 2
    correct = submit(ans_2, level=2, day=DAY, year=YEAR)