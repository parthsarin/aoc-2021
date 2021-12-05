"""
File: day-5.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *
from collections import defaultdict

DAY = 5
YEAR = 2021
data = get_input(write=True, day=DAY, year=YEAR)

# --- Part 1 ---
d = defaultdict(int) # (x, y) -> # of overlaps at that point
lines = data.split('\n')
for line in lines:
    start, end = line.split(' -> ')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    if x1 == x2:
        a, b = min(y1, y2), max(y1, y2)
        for y in range(a, b + 1):
            d[(x1, y)] += 1
    
    elif y1 == y2:
        a, b = min(x1, x2), max(x1, x2)
        for x in range(a, b + 1):
            d[(x, y1)] += 1

ans_1 = 0
for k, v in d.items():
    if v >= 2:
        ans_1 += 1    


# --- Part 2 ---

d = defaultdict(int)
for line in lines:
    start, end = line.split(' -> ')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    if x1 == x2:
        a, b = min(y1, y2), max(y1, y2)
        for y in range(a, b + 1):
            d[(x1, y)] += 1

    elif y1 == y2:
        a, b = min(x1, x2), max(x1, x2)
        for x in range(a, b + 1):
            d[(x, y1)] += 1

    else:
        m = (y2 - y1) / (x2 - x1)
        if m == -1:
            min_x, max_y = min(x1, x2), max(y1, y2)
            max_x = max(x1, x2)
            max_delta = max_x - min_x
            for delta in range(max_delta + 1):
                d[(min_x + delta, max_y - delta)] += 1

        elif m == 1:
            min_x, min_y = min(x1, x2), min(y1, y2)
            max_x = max(x1, x2)
            max_delta = max_x - min_x
            for delta in range(max_delta + 1):
                d[(min_x + delta, min_y + delta)] += 1

        else:
            print(f"Something went wrong: {m =}")

ans_2 = 0
for k, v in d.items():
    if v >= 2:
        ans_2 += 1    


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