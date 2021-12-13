"""
File: day-13.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *
import re

DAY = 13
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)


def fold_across(pt, fold_line):
  if pt < fold_line:
    return pt
  elif pt > fold_line:
    return fold_line - abs(pt - fold_line)
  else:
    raise ValueError("Point on line!")


def parse_dots(data):
  points = set()
  for line in data.split('\n'):
    if not line.strip():
      return points
    try:
      x, y = line.strip().split(',')
    except ValueError:
      print(repr(line))
    x, y = int(x), int(y)
    points.add((x, y))

  return points


dots = parse_dots(data)

folds = re.findall(r'fold along (x|y)=(\d+)', data)
folds = [(l, int(val)) for l, val in folds]
for fold in folds:
  new_s = set()
  if fold[0] == 'x':
    def process(point, fold_line):
      x, y = point
      x, y = fold_across(x, fold_line), y
      return x, y
  else:
    def process(point, fold_line):
      x, y = point
      x, y = x, fold_across(y, fold_line)
      return x, y

  for dot in dots:
    new_dot = process(dot, fold[1])
    new_s.add(new_dot)

  dots = new_s
  break

ans_1 = len(dots)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)

dots = parse_dots(data)

folds = re.findall(r'fold along (x|y)=(\d+)', data)
folds = [(l, int(val)) for l, val in folds]
for fold in folds:
  new_s = set()
  if fold[0] == 'x':
    def process(point, fold_line):
      x, y = point
      x, y = fold_across(x, fold_line), y
      return x, y
  else:
    def process(point, fold_line):
      x, y = point
      x, y = x, fold_across(y, fold_line)
      return x, y

  for dot in dots:
    new_dot = process(dot, fold[1])
    new_s.add(new_dot)

  dots = new_s

xs = [t[0] for t in dots]
ys = [t[1] for t in dots]

max_x, max_y = max(xs), max(ys)
for y in range(max_y + 1):
  for x in range(max_x + 1):
    if (x, y) in dots:
      print('x', end='')
    else:
      print(' ', end='')
  print()


ans_2 = 'RGZLBHFP'

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 13   00:12:02    605      0   00:22:28   1145      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)
