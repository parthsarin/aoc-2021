"""
File: day-8.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *

DAY = 8
YEAR = 2021
data = get_input(write=True, day=DAY, year=YEAR)

# --- Part 1 ---
lines = data.split('\n')
ans_1 = 0
for line in lines:
    i, o = line.split(' | ')
    o = o.split(' ')
    o = [x for x in o if len(x) in {2, 3, 4, 7}]
    ans_1 += len(o)

# --- Part 2 ---
ACTIVE_TO_N = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}
N_TO_ACTIVE = {v:k for k, v in ACTIVE_TO_N.items()}
TARGET_LETTERS = list(ACTIVE_TO_N.keys())


def assign_letters(candidates, so_far, o):
    remaining = set(candidates.keys() - so_far.keys())
    if len(remaining) == 0:
        o.append(so_far)
        return

    x = remaining.pop()
    for ch in candidates[x]:
        if ch in so_far.values():
            continue

        new_so_far = {**so_far, x: ch}
        assign_letters(candidates, new_so_far, o)

    return False


def convert_to_num(letters):
    l = ''.join(sorted(letters))
    return ACTIVE_TO_N[l]


def solve_line(line):
    candidates = {
        'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    }
    i, o = line.split(' | ')
    o = o.split(' ')
    i = i.split(' ')
    n = i + o
    for x in n:
        letters = set()
        for l in TARGET_LETTERS: 
            if len(l) == len(x):
                letters = letters.union(set(l))
        for ch in x:
            candidates[ch] = candidates[ch].intersection(letters)
    
    res = []
    assign_letters(candidates, {}, res)

    for assignment in res:
        try:
            s = ''
            for x in o:
                x = ''.join(sorted([assignment[ch] for ch in x]))
                digit = ACTIVE_TO_N[x]
                s += str(digit)
            return int(s)
        except KeyError:
            continue

ans_2 = 0
for line in lines:
    ans_2 += solve_line(line)

"""
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  8   00:03:16    51     50   00:34:43   617      0
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