"""
File: day-1.py
--------------
"""

s = open('../inputs/day-1.txt', 'r').read()
n = [int(i) for i in s.split()]

def compute_inc(lst):
    # I know summing booleans isn't good style, but cut me some slack :)
    return sum((a < b for a, b in zip(lst, lst[1:])))

print(compute_inc(n))

triples = [sum(t) for t in zip(n, n[1:], n[2:])]
print(compute_inc(triples))
