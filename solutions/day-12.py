"""
File: day-12.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from collections import defaultdict
import collections
from utils import *

DAY = 12
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)
maze = defaultdict(list)
for line in data.split('\n'):
    line = line.strip()
    l, r = line.split('-')
    maze[l].append(r)
    maze[r].append(l)

# Recursively explore all paths
def explore_paths(curr_path, maze, paths, visited):
    curr_node = curr_path[-1]
    if curr_node == 'end':
        paths.append(curr_path)
        return paths

    for next_node in maze[curr_node]:
        if (next_node not in visited) or next_node.isupper():
            # Visit big caves or new nodes
            if not next_node.isupper():
                visited.add(next_node)
            explore_paths(curr_path + [next_node], maze, paths, visited)
            if not next_node.isupper():
                visited.remove(next_node)
    
    return paths

all_paths = []
explore_paths(['start'], maze, all_paths, {'start'})

ans_1 = len(all_paths)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
maze = defaultdict(list)
for line in data.split('\n'):
    line = line.strip()
    l, r = line.split('-')
    maze[l].append(r)
    maze[r].append(l)


all_paths = []
stack = []
for next_node in maze['start']:
    stack.append(['start', next_node])

while stack:
    curr_path = stack.pop()
    curr_node = curr_path[-1]
    if curr_node == 'end':
        all_paths.append(curr_path)
        continue

    small_limit = defaultdict(int)
    for node in curr_path:
        if node.islower():
            small_limit[node] += 1
    small_limit = any(v == 2 for v in small_limit.values())

    for next_node in maze[curr_node]:
        if next_node in curr_path and next_node.islower() and small_limit:
            continue
        
        if next_node == 'start':
            continue
        
        stack.append(curr_path + [next_node])

ans_2 = len(all_paths)

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 12   00:09:35    315      0   00:28:38   1085      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)