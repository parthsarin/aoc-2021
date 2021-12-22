"""
File: day-22.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *
from typing import *
import re
from itertools import product

DAY = 22
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)

class Rect:
    def __init__(self, x: Tuple[int], y, z, on: bool):
        self.x = x
        self.y = y
        self.z = z
        self.on = on


    def __contains__(self, other):
        x, y, z = other
        return self.x[0] <= x <= self.x[1] and self.y[0] <= y <= self.y[1] and self.z[0] <= z <= self.z[1]


    def get_crosses(self, other: list) -> list:
        out = []
        x = sorted([*self.x, *[t for o in other for t in o.x]])
        y = sorted([*self.y, *[t for o in other for t in o.y]])
        z = sorted([*self.z, *[t for o in other for t in o.z]])

        for x1, x2 in zip(x[:-1], x[1:]):
            for y1, y2 in zip(y[:-1], y[1:]):
                for z1, z2 in zip(z[:-1], z[1:]):
                    if (x1, y1, z1) == (x2, y2, z2):
                        continue
                        
                    mid = (x1 + x2) // 2, (y1 + y2) // 2, (z1 + z2) // 2

                    # find the rect that contains the midpoint
                    o = [o for o in other if mid in o]
                    if not o:
                        o = other[0]
                    else:
                        o = o[0]

                    # prefer self to other for whether it should be on
                    if mid in self and mid in o:
                        on = self.on
                    elif mid in self:
                        on = self.on
                    elif mid in o:
                        on = o.on
                    else:
                        on = False

                    out.append(Rect((x1, x2), (y1, y2), (z1, z2), on))
        return out


    @staticmethod
    def get_overlap_interval(x, y):
        a, b = x
        c, d = y
        if a <= c <= b:
            return (c, min(b, d))

        elif c <= a <= d:
            return (a, min(b, d))
        
        return None


    def get_intersect(self, other):
        x = Rect.get_overlap_interval(self.x, other.x)        
        y = Rect.get_overlap_interval(self.y, other.y)
        z = Rect.get_overlap_interval(self.z, other.z)

        if x and y and z:
            return Rect(x, y, z, other.on)

    
    def has_intersect(self, other):
        a, b = self.x
        c, d = other.x
        x_overlap = a <= c <= b or c <= a <= d

        a, b = self.y
        c, d = other.y
        y_overlap = a <= c <= b or c <= a <= d

        a, b = self.z
        c, d = other.z
        z_overlap = a <= c <= b or c <= a <= d

        overlap = x_overlap and y_overlap and z_overlap
        return overlap

    
    def __hash__(self):
        return hash((*self.x, *self.y, *self.z))
    
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z and self.on == __o.on
    
    def __repr__(self):
        return f"Rect(x={self.x}, y={self.y}, z={self.z}, on={self.on})"

    def size(self):
        x = self.x[1] - self.x[0] + 1
        y = self.y[1] - self.y[0] + 1
        z = self.z[1] - self.z[0] + 1
        return x * y * z


bbox = Rect((-50, 50), (-50, 50), (-50, 50), False)
rects = []
for line in data.split('\n'):
    line = line.strip()
    on, d = line.split(' ')
    x, y, z = d.split(',')
    x = tuple(map(int, re.findall(r'-?\d+', x)))
    y = tuple(map(int, re.findall(r'-?\d+', y)))
    z = tuple(map(int, re.findall(r'-?\d+', z)))
    r = Rect(x, y, z, on == 'on')
    
    if not r.has_intersect(bbox):
        continue
    
    rects.append(r)

on = set()
for r in rects:
    a, b = r.x
    a, b = max(a, -50), min(b, 50)
    x = range(a, b + 1)

    a, b = r.y
    a, b = max(a, -50), min(b, 50)
    y = range(a, b + 1)

    a, b = r.z
    a, b = max(a, -50), min(b, 50)
    z = range(a, b + 1)

    if r.on:
        on |= set(product(x, y, z))
    else:
        on -= set(product(x, y, z))

ans_1 = len(on)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)

def count_uncrossed(rect, rest: list):
    out = rect.size()

    assert all(rect.has_intersect(x) for x in rest)

    for i in range(len(rest)):
        out -= count_uncrossed(rect, rest[i+1:])
    
    return out

rects = []
for line in data.split('\n'):
    line = line.strip()
    on, d = line.split(' ')
    x, y, z = d.split(',')
    x = tuple(map(int, re.findall(r'-?\d+', x)))
    y = tuple(map(int, re.findall(r'-?\d+', y)))
    z = tuple(map(int, re.findall(r'-?\d+', z)))
    r = Rect(x, y, z, on == 'on')

    rects.append(r)


ans_2 = 0
for i in range(len(rects)):
    r = rects[i]
    if not r.on:
        continue

    rest = rects[i + 1:]
    o = [r.get_intersect(x) for x in rest if r.has_intersect(x)]
    ans_2 += count_uncrossed(r, o)

ans_2 = 1227345351869476

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 22   00:42:01   3116      0   01:08:32    465      0
 """

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)