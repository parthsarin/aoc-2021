"""
File: day-.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *

data = get_input(write = True)

# --- Part 1 ---
ans_1 = None

# --- Part 2 ---
ans_2 = None

# --- Submission Code ---
if not os.path.exists(f'../puzzles/day-{day_idx}.md'):
    # Level 2 hasn't been generated yet; we're on level 1
    correct = submit(ans_1, level=1)
    if correct:
        puzzle = get_puzzle()
        with open(f'../puzzles/day-{day_idx}.md', 'w') as f:
            f.write(puzzle)
else:
    # Level 2 has been generated; we're on level 2
    correct = submit(ans_2, level=2)