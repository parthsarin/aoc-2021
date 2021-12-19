"""
File: day-.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *
from collections import namedtuple, defaultdict
from itertools import combinations, product
import pickle
import numpy as np

DAY = 19
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = data.split('\n')
Point = namedtuple('Point', ['x', 'y', 'z'])
Orientation = namedtuple('Orientation', ['x', 'y', 'z'])

points = []
new_l = True
for line in data:
    if not line or line.startswith('---'):
        new_l = True
        continue
    
    if new_l:
        points.append([])
        new_l = False
    
    l = points[-1]
    l.append(Point(*map(int, line.split(','))))

def dist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)
    
distances = []
for scanner in points:
    distances.append({})
    for p1, p2 in combinations(scanner, 2):
        distances[-1][(p1, p2)] = dist(p1, p2)


# matches = defaultdict(list)

# for i in range(len(distances)):
#     for j in range(i+1, len(distances)):
#         s1 = distances[i]
#         s2 = distances[j]

#         overlapping = []

#         # need to check for overlapping points
#         for p1 in points[i]:
#             for p2 in points[j]:
#                 # is p1 == p2?
#                 p1_dist = {k: v for k, v in s1.items() if p1 in k}
#                 p2_dist = {k: v for k, v in s2.items() if p2 in k}

#                 overlap = set(p1_dist.values()) & set(p2_dist.values())
#                 if len(overlap) >= 11:
#                     # this point and the 11 others are candidates
#                     overlapping.append((p1, p2))

#         if len(overlapping) >= 12:
#             # we have a winner!
#             print(f'{i} <--> {j}')
#             matches[i].append((j, overlapping))
#             matches[j].append((i, overlapping))

# pickle.dump(matches, open('../data/day-19.pkl', 'wb'))

matches = pickle.load(open('../data/day-19.pkl', 'rb'))

all_orients = []
x = np.array([1, 0, 0])
y = np.array([0, 1, 0])
z = np.array([0, 0, 1])
for x_dir in (x, -x, y, -y, z, -z):
    rem = [x, y, z]
    rem = [d for d in rem if not all(d == abs(x_dir))]
    for y_dir in rem:
        for mul in (+1, -1):
            y_dir = mul * y_dir
            z_dir = np.cross(x_dir, y_dir)
            all_orients.append(Orientation(x_dir, y_dir, z_dir))


def apply_orient(orient, point):
    return point.x * orient.x + point.y * orient.y + point.z * orient.z


def deduce_pos(
        overlap=[]
    ):
    # assume s1 is (0, 0, 0) and +x, +y, +z
    s1 = [pair[0] for pair in overlap]
    s2 = [pair[1] for pair in overlap]
    for s2_orient in all_orients:
        p1, p2 = s1[0], s2[0]
        p2 = apply_orient(s2_orient, p2)

        delta = np.array([p1.x, p1.y, p1.z]) - p2
        s2_adj = [delta + apply_orient(s2_orient, p) for p in s2]
        
        recovered = set(map(tuple, s2_adj)) & set(s1)
        if len(recovered) >= 12:
            return delta, s2_orient


all_pts = set()
visited = {0}
stack = [[0]]
while stack:
    path = stack.pop()
    pt = path[-1]
    visited.add(pt)

    # convert points back to original orientation
    bad_pts = points[pt]
    rev_path = path[::-1]
    for a, b in zip(rev_path, rev_path[1:]):
        # convert from a to b
        _, overlap = next(t for t in matches[a] if t[0] == b)

        if b > a:
            overlap = [(t[1], t[0]) for t in overlap]

        delta, a_orient = deduce_pos(overlap)
        bad_pts = [apply_orient(a_orient, p) + delta for p in bad_pts]
        bad_pts = [Point(*p) for p in bad_pts]
    
    if len(path) > 1:
        assert len(set(bad_pts) & all_pts) >= 12
    
    all_pts |= set(bad_pts)

    # add next points
    for i, overlap in matches[pt]:
        if i not in visited:
            stack.append(path + [i])

ans_1 = len(all_pts)

# --- Part 2 ---
ans_2 = max(dist(a, b) for a, b in combinations(all_pts, 2))

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 19   01:45:22    649      0   01:47:14    537      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)