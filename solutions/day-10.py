"""
File: day-10.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *

DAY = 10
YEAR = 2021
data = get_input(write=True, day=DAY, year=YEAR)

# --- Part 1 ---
lines = data.split('\n')
POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
INVERT = {'(': ')', '[': ']', '{': '}', '<': '>'}

def corrupted_pts(line):
    stack = []
    for ch in line:
        if ch in '({[<':
            stack.append(ch)
        elif ch in ')}]>':
            if not stack:
                return POINTS[ch]
            
            if (ch == ')' and stack[-1] != '(') \
                or (ch == ']' and stack[-1] != '[') \
                or (ch == '}' and stack[-1] != '{') \
                or (ch == '>' and stack[-1] != '<'):
                return POINTS[ch]
            
            stack.pop()
    
    return 0

ans_1 = sum(corrupted_pts(line) for line in lines)

# --- Part 2 ---
import numpy as np
POINTS = {')': 1, ']': 2, '}': 3, '>': 4}

def autocomplete(line):
    stack = []
    for ch in line:
        if ch in '({[<':
            stack.append(ch)
        elif ch in ')}]>':
            if not stack:
                return None
            
            if (ch == ')' and stack[-1] != '(') \
                or (ch == ']' and stack[-1] != '[') \
                or (ch == '}' and stack[-1] != '{') \
                or (ch == '>' and stack[-1] != '<'):
                return None
            
            stack.pop()

    if not stack:
        # Line is valid
        return None
    
    # Otherwise, autocomplete
    s = ''.join(INVERT[x] for x in stack[::-1])
    score = 0
    for ch in s:
        score *= 5
        score += POINTS[ch]

    return score


a_scores = [
    x 
    for line in lines 
    if (x := autocomplete(line)) is not None
]
ans_2 = int(np.median(a_scores))

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