"""
File: day-.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *
from collections import defaultdict
from copy import deepcopy
from itertools import product

DAY = 21
YEAR = 2021

# --- Part 1 ---
def die():
  state = 0
  while True:
    state = (state % 100) + 1
    yield state

class Board:
  def __init__(self):
    self.scores = defaultdict(int) # {player -> score}
    self.location = {1: 10, 2: 9}
    self.die = die()
    self.num_rolls = 0
    
  def advance(self, player):
    for _ in range(3):
      self.location[player] += next(self.die)
      self.num_rolls += 1

    while self.location[player] > 10:
      self.location[player] -= 10
    
    self.scores[player] += self.location[player]
  
  def advance_noroll(self, player, score):
    self.location[player] += score
    self.num_rolls += 1
    while self.location[player] > 10:
      self.location[player] -= 10
    
    self.scores[player] += self.location[player]
  
  @property
  def finished(self):
    return any(v >= 1000 for v in self.scores.values())
  

b = Board()

while not b.finished:
  b.advance(1)
  if not b.finished:
    b.advance(2)

ans_1 = b.num_rolls * min(b.scores.values())

"""
--- Part Two ---

Now that you're warmed up, it's time to play the real game.

A second compartment opens, this time labeled Dirac dice. Out of it falls a single three-sided die.

As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a quantum die: when you roll it, the universe splits into multiple copies, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.

The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least 21.

Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, while player 2 merely wins in 341960390180808 universes.

Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; in how many universes does that player win?
"""
rolls = [a + b + c for a, b, c in product(range(1, 4), repeat=3)]
memoization_is_the_best = {} # (l1, l2, s1, s2) -> (num_1, num_2)

def run(l1, l2, s1, s2):
  if s1 >= 21:
    return 1, 0
  if s2 >= 21:
    return 0, 1
  
  if (l1, l2, s1, s2) in memoization_is_the_best:
    return memoization_is_the_best[(l1, l2, s1, s2)]

  w1, w2 = 0, 0  
  for r in rolls:
    new_l1 = l1 + r
    while new_l1 > 10:
      new_l1 -= 10

    new_s1 = s1 + new_l1

    a, b = run(l2, new_l1, s2, new_s1) # Parth is a clever bunny 🐰
    w1 += b
    w2 += a
  
  memoization_is_the_best[(l1, l2, s1, s2)] = (w1, w2)
  return w1, w2


t = run(10, 9, 0, 0)
ans_2 = max(t)

"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 21   00:12:23   1040      0   01:00:06   1315      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)