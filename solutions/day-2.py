"""
File: day-2.py
--------------
"""

s = open('../inputs/day-2.txt')
pos = [0, 0] #[depth, forward/backward]
for line in s:
    line = line.strip()
    n = int(line[-1])
    if line.startswith("forward"):
        pos[1] += n
    elif line.startswith("down"):
        pos[0] += n
    else:
        pos[0] -= n

        
print(pos[0] * pos[1])


state = [0, 0, 0] #[aim, horizontal, depth]

for line in s:
    line = line.strip()
    n = int(line[-1])
    if line.startswith("forward"):
        state[1] += n
        state[2] += n * state[0]
    elif line.startswith("down"):
        state[0] += n
    else:
        state[0] -= n

print(state[1]*state[2])

"""
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  2   00:04:11  2268      0   00:06:46  2040      0
"""