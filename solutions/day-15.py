"""
File: day-15.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *
from collections import deque

DAY = 15
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)

def process(data):
    return [[int(x) for x in row.strip()] for row in data.split('\n')]

data = process(data)
n_row = len(data)
n_col = len(data[0])

def calc_lowest_risk(data):
    n_row = len(data)
    n_col = len(data[0])

    risk = [[0 for _ in range(n_col)] for __ in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            risk[i][j] = data[i][j]


    for i in range(n_row - 1, -1, -1):
        for j in range(n_col - 1, -1, -1):
            print(i, j, risk[i][j])
            n = []
            try:
                n.append(risk[i + 1][j])
            except IndexError:
                pass

            try:
                n.append(risk[i][j + 1])
            except IndexError:
                pass

            try:
                n.append(risk[i - 1][j])
            except IndexError:
                pass

            try:
                n.append(risk[i][j - 1])
            except IndexError:
                pass
            
            print(n)
            if n:
                risk[i][j] += min(n)

    risk[0][0] -= data[0][0]
    return risk[0][0]


ans_1 = calc_lowest_risk(data)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = process(data)

def expand(data):
    n_row = len(data)
    n_col = len(data[0])

    full_data = [[0 for _ in range(5 * n_col)] for __ in range(5 * n_row)]
    for i in range(5 * n_row):
        for j in range(5 * n_col):
            n = data[i % n_row][j % n_col]
            inc = i // n_row + j // n_col
            n = n + inc
            while n > 9:
                n -= 9
            full_data[i][j] = n
    
    return full_data


ans_2 = 2938

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 15   00:20:02   1148      0   00:48:22   1447      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)