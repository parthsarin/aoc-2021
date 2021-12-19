"""
File: day-18.py
---------------
For Level 1, use the website. For Level 2, use the file puzzles/day-...
"""
from utils import *

DAY = 18
YEAR = 2021

# --- Part 1 ---
data = get_input(write=True, day=DAY, year=YEAR)

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def __repr__(self):
        return f'Node({self.val})'


    def print(self, tabs=0):
        print('\t' * tabs, end = '')
        print(self)
        if self.left:
            self.left.print(tabs + 1)
        if self.right:
            self.right.print(tabs + 1)
    

    def depth(self, curr_depth = 0):
        x, y = curr_depth, curr_depth
        if self.left:
            x = self.left.depth(curr_depth + 1)
        if self.right:
            y = self.right.depth(curr_depth + 1)
        return max(x, y)

    
    def as_list(self):
        if self.val is None:
            return [self.left.as_list(), self.right.as_list()]
        else:
            return self.val


def add(num, other):
    o = Node(None)
    o.left = num
    o.right = other
    return o


def convert_lst(lst):
    if isinstance(lst, list):
        n = Node(None)
        n.left = convert_lst(lst[0])
        n.right = convert_lst(lst[1])
        return n
    else:
        return Node(lst)


def find_high_depth(root, threshold):
    l, r = -1, -1
    if root.left:
        l = root.left.depth()
    if root.right:
        r = root.right.depth()
    
    if l >= threshold:
        return 0, root.left
    elif r >= threshold:
        return 1, root.right


def iterate_depth(root):
    moves = []
    t = 4
    while t > 0:
        m, root = find_high_depth(root, t)
        moves.append(m)
        t -= 1
    
    return moves


def find_10(root, path = []):
    if root.val is not None and root.val >= 10:
        return path
    
    if root.left:
        p = find_10(root.left, path + [0])
        if p is not None:
            return p
    if root.right:
        p = find_10(root.right, path + [1])
        if p is not None:
            return p
    
    return None


def reduce(root):
    lst = root.as_list()
    changed = True
    while changed:
        # print(lst)
        root = convert_lst(lst)
        
        changed = False
        if root.depth() >= 5:
            # find leftmost such pair
            path = iterate_depth(root)
            assert len(path) == 4

            explode(root, lst, path)
            changed = True
            continue
        
        path = find_10(root)
        if path:
            changed = True
            split(lst, path)
    root = convert_lst(lst)
    return root

def traverseLst(lst, path):
  newSubLst = lst
  for i in path:
      newSubLst = newSubLst[i]
  return newSubLst

def split(lst, path):
    idx = path[-1]
    path = path[:-1]
    newSubLst = traverseLst(lst, path)
    
    leftNum = newSubLst[idx]//2
    rightNum = newSubLst[idx] - leftNum

    newSubSubLst = [leftNum, rightNum]
    newSubLst[idx] = newSubSubLst
    

def complete_path(root, path, skew = 0):
    for x in path:
        if x == 0:
            try:
                root = root.left
            except AttributeError:
                # invalid path
                return None
        else:
            try:
                root = root.right
            except AttributeError:
                return None
    
    if root is None:
        # invalid path
        return None
    
    new_path = path[:]
    while root.val is None:
        root = root.left if skew == 0 else root.right
        new_path.append(skew)
    
    return new_path
        

def get_left(root, path):
    new_path = path[:]
    for i in range(len(path) - 1, -1, -1):
        # try turning left here
        if path[i] == 1:
            new_path = path[:i] + [0]
            p = complete_path(root, new_path, 1)
            if p is not None:
                return p
            
            new_path = path[:]
        
        
def get_right(root, path):
    new_path = path[:]
    for i in range(len(path) - 1, -1, -1):
        # try turning right here
        if path[i] == 0:
            new_path = path[:i] + [1]
            p = complete_path(root, new_path, 0)
            if p is not None:
                return p


def explode(root, lst, path):
    idx = path[-1] 
    path = path[:-1]
    newSubLst = traverseLst(lst, path)

    if idx == 0:
        pathLeft = get_left(root, path)
        if pathLeft:
            leftSubPath = traverseLst(lst, pathLeft[:-1])
            leftSubPath[pathLeft[-1]] += newSubLst[0][0]
        # left_num = 0
        if isinstance(newSubLst[1], int):
            newSubLst[1] += newSubLst[0][1]
        else:
            newSubLst[1][0] += newSubLst[0][1]
        newSubLst[0] = 0
   
    else:
        pathRight = get_right(root, path)
        if pathRight:
            rightSubPath = traverseLst(lst, pathRight[:-1])
            rightSubPath[pathRight[-1]] += newSubLst[1][1]
          # left_num = newSubLst[1][0] + newSubLst[0]
        # right_num = 0
        if isinstance(newSubLst[0], int):
            newSubLst[0] += newSubLst[1][0]
        else:
            newSubLst[0][1] += newSubLst[0][1]
        newSubLst[1] = 0
    
    return lst


def magnitude(root):
    if root.val is not None:
        return root.val

    l, r = root.left, root.right
    return 3 * magnitude(l) + 2 * magnitude(r)


def addAll(data):
    root = data[0]
    for newTree in data[1:]:
        root = add(root, newTree)
        root = reduce(root)
    
    return root

def test():
    # ---- convert_lst ----
    data = [
        [1, 2],
        [[1, 2], 3],
        [9, [8, 7]],
        [[1, 9], [8, 5]],
        [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9],
        [[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]],
        [[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [
            [[4, 9], [6, 9]], [[8, 2], [7, 3]]]]
    ]

    for lst in data:
        root = convert_lst(lst)
        assert root.as_list() == lst

    # --- addition ---
    l1 = convert_lst([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
    l2 = convert_lst([1, 1])
    l = add(l1, l2)
    
    assert l.as_list() == [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]

    # --- explode check ---
    assert l.depth() >= 5
    assert iterate_depth(l) == [0, 0, 0, 0]

    # ---- find_10 ----
    n = convert_lst([[[[0, 7], 4], [15, [0, 13]]], [1, 1]])
    assert find_10(n) == [0, 1, 0]
    
    # ---- get_left & get_right ----
    l = [ [ [ [0,7], 4 ], [ 7, [ [8,4], 9 ] ] ], [1,1] ]
    path = [0, 1, 1, 0]
    l = get_left(convert_lst(l), path)
    assert l == [0, 1, 0]
    
    l = [ [ [ [ 0, 7 ], 4 ], [ [ 7, 8 ], [ 0, [ 6, 7 ] ] ] ], [ 1, 1 ] ]
    path = [0, 1, 1, 1]
    l = get_right(convert_lst(l), path)
    assert l == [1, 0]

    # ---- explode ----
    r = convert_lst([[[[[9, 8], 1], 2], 3], 4]) 
    newR = reduce(r).as_list() 
    assert newR == [[[[0, 9], 2], 3], 4]

    # ---- full reduce ----
    l = convert_lst([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]])
    l = reduce(l).as_list()
    assert l == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

    # ---- sample homework ----
    l = [
        [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
        [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
        [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
        [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
        [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
        [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
        [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
        [[9, 3], [[9, 9], [6, [4, 9]]]],
        [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
        [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]]
    ]
    l = [convert_lst(x) for x in l]
    root = addAll(l)
    assert root.as_list() == [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
    assert magnitude(root) == 4140


test()

data = data.split('\n')
data = [eval(x) for x in data]
data = [convert_lst(x) for x in data]
root = addAll(data)     
ans_1 = magnitude(root)

# --- Part 2 ---
data = get_input(write=True, day=DAY, year=YEAR)
data = data.split('\n')
data = [eval(x) for x in data]
data = [convert_lst(x) for x in data]

all_sums = []
for i in range(len(data)):
    for j in range(len(data)):
        if j != i:
            root = add(data[i], data[j])
            root = reduce(root)
            all_sums.append(magnitude(root))

ans_2 = max(all_sums)


"""
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 18   01:43:36   1277      0   01:46:35   1153      0
"""

# --- Submission Code ---
full_submit(ans_1=ans_1, ans_2=ans_2, day=DAY, year=YEAR, show_rank=False)