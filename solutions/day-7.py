"""
File: day-7.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *

DAY = 7
YEAR = 2021
data = get_input(write=True, day=DAY, year=YEAR)

# --- Part 1 ---
data = [int(t) for t in data.split(',')]
costs = []
for idx in range(max(data) + 1):
    # test aligning to this position
    cost = sum(abs(pos - idx) for pos in data)
    costs.append(cost)
ans_1 = min(costs)

# --- Part 2 ---
def cost_to_move(pos, idx):
    # crab is at pos, move to idx
    a, b = min(pos, idx), max(pos, idx)
    top = b - a
    cost = top * (1 + top) / 2
    return cost


costs = []
for idx in range(max(data) + 1):
    # test aligning to this position
    cost = 0
    for pos in data: 
        cost += cost_to_move(pos, idx)
    costs.append(int(cost))

ans_2 = min(costs)

"""
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  7   00:02:14   188      0   00:06:50   744      0
"""

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