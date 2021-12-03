"""
File: day-4.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *

data = get_input(write = True, day=4, year=2021)

# --- Part 1 ---
ans_1 = None

# --- Part 2 ---
ans_2 = None

# --- Submission Code ---
if not os.path.exists(f'../puzzles/day-4.md'):
    # Level 2 hasn't been generated yet; we're on level 1
    correct = submit(ans_1, level=1, day=4, year=2021)
    if correct:
        puzzle = get_puzzle(day=4, year=2021)
        with open(f'../puzzles/day-4.md', 'w') as f:
            f.write(puzzle)
else:
    # Level 2 has been generated; we're on level 2
    correct = submit(ans_2, level=2, day=4, year=2021)