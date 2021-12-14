"""
File: day-14.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *
from collections import Counter, defaultdict

DAY = 14
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = data.split('\n')
polymer = data[0]

rules = {}
for rule in data[2:]:
    i, o = rule.split(' -> ')
    a, b = list(i)
    rules[(a, b)] = o

for step in range(10):
    new_polymer = ''
    for a, b in zip(polymer, polymer[1:]):
        if (a, b) in rules:
            o = rules[(a, b)]
            new_polymer += a + o
        else:
            new_polymer += a
    new_polymer += polymer[-1]
    polymer = new_polymer

p = Counter(polymer)
x, y = p.most_common(1)[0], p.most_common()[-1]
ans_1 = x[1] - y[1]

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = data.split('\n')

rules = {}
for rule in data[2:]:
    i, o = rule.split(' -> ')
    a, b = list(i)
    rules[(a, b)] = o

polymer = defaultdict(int)
polymer_s = data[0]
for a, b in zip(polymer_s, polymer_s[1:]):
    polymer[(a, b)] += 1

for step in range(40):
    print(step, sum(polymer.values()))
    new_polymer = defaultdict(int)
    for (a, b), v in rules.items():
        if (a, b) in polymer:
            n = polymer.pop((a, b))
            new_polymer[(a, v)] += n
            new_polymer[(v, b)] += n

    polymer = {**polymer, **new_polymer}

counts = defaultdict(int)
for (a, b), v in polymer.items():
    counts[a] += v
counts[polymer_s[-1]] += 1

ans_2 = max(counts.values()) - min(counts.values())

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 14   00:10:02    824      0   00:21:47    469      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)