from random import sample
base = 3
side = base*base

# Pattern for a baselinevalid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

# Randomize rows, columns and numbers (of valid base pattern)

def shuffle(s):
    return sample(s,len(s))

rBase = range(base)
rows = [g*base+r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g*base+c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1,base*base+1))

# Produce board using randomized baseline pattern
board = [[nums[pattern(r,c)]for c in cols]for r in rows]

def print_board():
    for line in board:
        i=0
        row_sep = '-'*35
        if i%3==0:
            print(row_sep)      
        print(*(f"{n or ' ':{0}} |" for n in line))

print_board()

squares = side*side # = 81
empties = squares * 3//4 # = 60
for p in sample(range(squares), empties): # 60 boxes will be empty
    board[p//side][p%side] = 0            # random box from 60 boxes

numSize = len(str(side))
for line in board:
    i=0
    row_sep = '-'*35
    if i%3==0:
        print(row_sep) 
    print(*(f"{n or ' ':{numSize}} |" for n in line))
