"""
File: day-6.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *
from collections import defaultdict

DAY = 6
YEAR = 2021
data = get_input(write=True, day=DAY, year=YEAR)

# --- Part 1 ---
fish = [int(d) for d in data.split(',')]

for day in range(80):
    new_fish = []
    for age in fish:
        # new_age = age - 1
        if age == 0:
            new_age = 6
            new_fish.append(8)
        else:
            new_age = age - 1
        new_fish.append(new_age)
    fish = new_fish
    
ans_1 = len(fish)

# --- Part 2 ---
fish = [int(d) for d in data.split(',')]
d = {age: fish.count(age) for age in set(fish)}

for day in range(256):
    new_d = {(k-1):v for k, v in d.items()}
    num_old = new_d.pop(-1, 0)
    new_d[6] = new_d.get(6, 0) + num_old
    new_d[8] = new_d.get(8, 0) + num_old
    d = new_d

ans_2 = sum(d.values())

"""
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  6   00:04:26   417      0   00:09:53   452      0
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