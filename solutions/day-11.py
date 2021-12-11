"""
File: day-11.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *
from itertools import product

DAY = 11
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = data.split('\n')
data = [list(map(int, list(x))) for x in data]
n_rows = len(data)
n_cols = len(data[0])

def get_neighbors(i, j):
    candidates = [
        (i - 1, j), (i + 1, j),
        (i, j - 1), (i, j + 1),
        (i - 1, j - 1), (i + 1, j + 1),
        (i + 1, j - 1), (i - 1, j + 1)
    ]

    candidates = [
        (i, j)
        for i, j in candidates
        if 0 <= i < n_rows and 0 <= j < n_cols
    ]

    return candidates

def coord_nine(data):
    o = []
    for i in range(n_rows):
        for j in range(n_cols):
            if data[i][j] > 9:
                o.append((i, j))
    return set(o)

num_flashed = 0
for step in range(100):
    flashed = set()
    data = [[x + 1 for x in row] for row in data]

    while (nines := coord_nine(data) - flashed):
        for i, j in nines:
            flashed.add((i, j))

            n = get_neighbors(i, j)
            for x, y in n:
                if data[x][y] < 10:
                    data[x][y] += 1
    
    num_flashed += len(flashed)
    for i, j in flashed:
        data[i][j] = 0

ans_1 = num_flashed

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = data.split('\n')
data = [list(map(int, list(x))) for x in data]
n_rows = len(data)
n_cols = len(data[0])

step = 0
while True:
    step += 1
    flashed = set()
    data = [[x + 1 for x in row] for row in data]

    while (nines := coord_nine(data) - flashed):
        for i, j in nines:
            flashed.add((i, j))

            n = get_neighbors(i, j)
            for x, y in n:
                if data[x][y] < 10:
                    data[x][y] += 1

    for i, j in flashed:
        data[i][j] = 0
    
    if all(data[i][j] == 0 for i, j in product(range(n_rows), range(n_cols))):
        break

ans_2 = step

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 11   00:13:04    467      0   00:23:29   1300      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)