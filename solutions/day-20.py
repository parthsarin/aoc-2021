"""
File: day-20.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *

DAY = 20
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = iter(data.split('\n'))
decoder = next(data).strip()
next(data)

img = list(data)
img = [list(x.strip()) for x in img]
img = [[p == '#' for p in row] for row in img]

class Image:
    def __init__(self, base_img=None):
        self.lit = set()

        for i in range(len(base_img)):
            for j in range(len(base_img[0])):
                if base_img[i][j]:
                    self.lit.add((i, j))
    
        self.boundary = False


    def update_min_max(self):
        self.min_i = min(x[0] for x in self.lit)
        self.max_i = max(x[0] for x in self.lit)
        self.min_j = min(x[1] for x in self.lit)
        self.max_j = max(x[1] for x in self.lit)


    def is_lit(self, i, j):
        if i < self.min_i or i > self.max_j:
            return self.boundary
        if j < self.min_j or j > self.max_j:
            return self.boundary

        return (i, j) in self.lit

    def enhance(self):
        self.update_min_max()
        min_i, max_i = self.min_i, self.max_i
        min_j, max_j = self.min_j, self.max_j

        new_lit = set()

        for i in range(min_i - 5, max_i + 5):
            for j in range(min_j - 5, max_j + 5):
                nbr = [
                    (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                    (i, j - 1), (i, j), (i, j + 1),
                    (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                ]

                nbr = [int(self.is_lit(*x)) for x in nbr]
                nbr = map(str, nbr)
                nbr = int(''.join(nbr), 2)
                
                is_lit = decoder[nbr] == '#'
                if is_lit:
                    new_lit.add((i, j))
        
        self.boundary = not self.boundary
        self.lit = new_lit


img = Image(img)
img.enhance()
img.enhance()
ans_1 = len(img.lit)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = iter(data.split('\n'))
decoder = next(data).strip()
next(data)

img = list(data)
img = [list(x.strip()) for x in img]
img = [[p == '#' for p in row] for row in img]

img = Image(img)
for i in range(50):
    img.enhance()

ans_2 = len(img.lit)

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 20   00:18:15    143      0   00:19:08    104      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)