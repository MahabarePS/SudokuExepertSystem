import numpy as np
import random

# Generating 9x9 matrix of sudoku
board_zeros = np.zeros(shape=(9,9), dtype=int)
#print(board_zeros)

# Let's make a board a bit user friendly by dividing it into 3x3 sub matrices
def board_print(board):

    # We will make sure the Sudoku table facts are followed
    assert board.shape == (9,9)
    assert type(board) == np.ndarray

    # We need to convert the array elements to string
    board_str = board.astype(str)

    # We will seperate rows with "-"
    row_sep = '-'*25

    # Since the Matrix is 9x9 we will iterate it 9 times
    for i in range(9):

        # At each multiple of 3, print row seperator
        if i%3 == 0:
            print(row_sep)

        # Getting the row data in string board
        row = board_str[i]

        # Arranging the print
        print('| '+' '.join(row[0:3])+' | '+ ' '.join(row[3:6])+ ' | '+' '.join(row[6:])+' |')

    #final print
    print(row_sep)

# Printing the final output with graphically arranged zeros
#board_print(board_zeros)

# Lets randomly generate the Sudoku puzzle
board_init = board_zeros.copy()
for i in range(9):
    board_init[i,random.randint(1,8)] = random.randint(1,5)
    for i in range(9):
         board_init[i,random.randint(1,8)] = random.randint(5,9)
print(board_print(board_init))