"""
File: day-17.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *

DAY = 17
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)

TARGET_X = (34, 67)
TARGET_Y = (-215, -186)

def one_step(pos, vel):
    x, y = pos
    vx, vy = vel
    new_pos = (x + vx, y + vy)
    
    if vx > 0:
        new_vel = (vx - 1, vy - 1)
    elif vx == 0:
        new_vel = (0, vy - 1)
    else:
        new_vel = (vx + 1, vy - 1)
    
    return new_pos, new_vel


def validate_route(route):
    for t in route:
        x, y = t
        x_valid = TARGET_X[0] <= x <= TARGET_X[1]
        y_valid = TARGET_Y[0] <= y <= TARGET_Y[1]
        if x_valid and y_valid:
            return True
    return False

def max_y(route):
    return max(t[1] for t in route)


def test_vel(x, y):
    pos = (0,0)
    vel = (x, y)
    poses = [(0,0)]
    while pos[0] < TARGET_X[1] and pos[1] > TARGET_Y[1]:
        pos, vel = one_step(pos, vel)
        poses.append(pos)
    
    if validate_route(poses):
        return max_y(poses) 
    else:
        return None

ans_1 = max(
    a
    for x in range(0, 68) 
    for y in range(0, 500)
    if (a := test_vel(x, y)) is not None
)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
ans_2 = len([
    a
    for x in range(0, 68)
    for y in range(-215, 500)
    if (a := test_vel(x, y)) is not None
])

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 17   00:12:57    361      0   00:15:14    202      0
"""

# --- Submission Code ---
print(ans_1, ans_2)
# full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)
