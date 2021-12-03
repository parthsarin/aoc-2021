"""
File: day-3.py
--------------
"""
import numpy as np

# --- Part One  ---
f = open('../inputs/day-3.txt')
i = 0
mat = []
for line in f:
    line = line.strip()
    mat.append([int(_) for _ in line])
mat = np.asarray(mat)
totals = np.sum(mat, axis=0)
gamma = [
    1 if totals[i] > mat.shape[0]/2 else 0 
    for i in range(len(totals))
]
epsilon = [1 if x == 0 else 0 for x in gamma]

gamma = int("".join(str(x) for x in gamma), 2)
epsilon = int("".join(str(x) for x in epsilon), 2)


print(gamma * epsilon)

# --- Part Two ---
f = open('../inputs/day-3.txt')
lines = f.read().strip().split('\n')

n = len(lines[0])
oxygen = lines[:]
for i in range(n):
    # filter out values that don't match the bit criteria
    chars = [s[i] for s in oxygen]
    z, o = chars.count('0'), chars.count('1')
    if z > o:
        oxygen = [s for s in oxygen if s[i] == '0']
    elif o > z:
        oxygen = [s for s in oxygen if s[i] == '1']
    else:
        oxygen = [s for s in oxygen if s[i] == '1']
    
    # if there is only one value left, stop
    if len(oxygen) == 1:
        break

oxygen = oxygen[0]

co2 = lines[:]
for i in range(n):
    # filter out values that don't match the bit criteria
    chars = [s[i] for s in co2]
    z, o = chars.count('0'), chars.count('1')
    if z > o:
        co2 = [s for s in co2 if s[i] == '1']
    elif o > z:
        co2 = [s for s in co2 if s[i] == '0']
    else:
        co2 = [s for s in co2 if s[i] == '0']

    # if there is only one value left, stop
    if len(co2) == 1:
        break
co2 = co2[0]

oxygen = int(oxygen, 2)
co2 = int(co2, 2)

print(oxygen * co2)

"""
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  3   00:08:06  1935      0   00:26:19  1863      0
"""
