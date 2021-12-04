"""
File: day-4.py
--------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
import os
from utils import *

data = get_input(write = True, day=4, year=2021)

# --- Part 1 ---
class BingoBoard:
    def __init__(self, rows):
        # Rows is a list of lists
        self.rows = [[int(it) for it in cols] for cols in rows]
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])
        self.marked = [
            [False for _ in range(self.num_cols)] 
            for _ in range(self.num_rows)
        ]
    
    def call(self, val):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.rows[i][j] == val:
                    self.marked[i][j] = True

    @property
    def hasWon(self):
        cols = [
            list(map(lambda x: x[i], self.marked)) 
            for i in range(len(self.rows[0]))
        ]
        if any(map(lambda x: all(x), cols)) or any(map(lambda x: all(x), self.marked)):
            return True
    
    @property
    def unmarked(self):
        return [
            [self.rows[i][j] for j in range(self.num_cols) if not self.marked[i][j]] 
            for i in range(self.num_rows)
        ]
    
    def __eq__(self, other):
        return self.rows == other.rows

lines = data.split('\n\n')
moves = lines[0]

all_boards = []
for board in lines[1:]:
    rows = board.split("\n")
    board = [row.strip().split() for row in rows]
    board = [list(map(int, row)) for row in board]
    board = BingoBoard(board)
    all_boards.append(board)

winning_board = None
moves = moves.split(",")
for move in moves:
    move = int(move)
    for board in all_boards:
        board.call(move)
    
    if any((board.hasWon for board in all_boards)):
        winning_board = next(((board for board in all_boards if board.hasWon)))
        break


sum_unmarked = sum((sum(r) for r in winning_board.unmarked))
ans_1 = sum_unmarked * move

# --- Part 2 ---
lines = data.split('\n\n')
moves = lines[0]

all_boards = []
for board in lines[1:]:
    rows = board.split("\n")
    board = [row.strip().split() for row in rows]
    board = [list(map(int, row)) for row in board]
    board = BingoBoard(board)
    all_boards.append(board)

winning_board = None
moves = moves.split(",")
for move in moves:
    move = int(move)

    if len(all_boards) > 1:
        for board in all_boards:
            board.call(move)
    
        all_boards = [board for board in all_boards if not board.hasWon]
    
    else:
        losing_board = all_boards[0]
        if not losing_board.hasWon:
            board.call(move)
            break

sum_unmarked = sum((sum(r) for r in losing_board.unmarked))
ans_2 = sum_unmarked * move

# --- Submission Code --- 
if not os.path.exists(f'../puzzles/day-4.md'):
    # Level 2 hasn't been generated yet; we're on level 1
    correct = submit(ans_1, level=1, day=4, year=2021)
    if correct:
        puzzle = get_puzzle(day=4, year=2021)
        with open(f'../puzzles/day-4.md', 'w') as f:
            f.write(puzzle)
else:
    # Level 2 has been generated; we're on level 2
    correct = submit(ans_2, level=2, day=4, year=2021)