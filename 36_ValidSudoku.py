# LeetCode Problem 36: Valid Sudoku
# Determine if a 9 x 9 Sudoku Board is valid.
# Only the filled cells need to be validated
# according to the following rules:
# - Each row must contain the digits 1 - 9 
# without repetition
# - Each column must contain the digits 1 - 9
# without repetition
# - Each of the nine 3 x 3 sub-boxes of the grid
# must contain the digits 1 - 9 without repetition
# Note: 
# - A Sudoku board (partially filled) could be valid
# but not necessarily solvable
# - Only the filled cells need to be validated
# according to the mentioned rules

# -------------------------------------------------------------
# SOLUTION 1: Brute Force
#   Check the rows, columns, and squares with sub-functions. The
#   board is not big enough require a faster solution.
def isValidSudoku( board ):
    # Number of rows and columns is predefined, making
    # our task much easier. Iterate through each row
    # and column, as well as square, and validate each
    # requirement of the board.
    for i in range( 9 ):
        if checkRowValid( board, i ) != True:
            return False
    
    for j in range( 9 ):
        if checkColValid( board, j ) != True:
            return False
        
    for i in range( 3 ):
        for j in range( 3 ):
            if checkSquareValid( board, i, j ) != True:
                return False

    return True


def checkRowValid( board, row ):
    curr_row = board[ row ][ : ]
    if curr_row.count( "." ) == 9:
        return False
    for i in range( 9 ):
        if curr_row[ i ] != ".":
            if curr_row.count( curr_row[ i ] )  > 1:
                return False
    return True


def checkColValid( board, col ):
    curr_col = board[ : ][ col ]
    for i in range( 9 ):
        if curr_col[ i ] != ".":
            if curr_col.count( curr_col[ i ] )  > 1:
                return False
    return True


def checkSquareValid( board, row, col ):
    # Note: Multi-Axis Slicing is not possible with lists,
    # so we have to do it mildly manually
    curr_square = [ ]
    for i in range( 3 ):
        for j in range( 3 ):
            curr_square.append( board[ i ][ j ] )
    
    for i in range( 9 ):
        if curr_square[ i ] != ".":
            if curr_square.count( curr_square[ i ] )  > 1:
                return False
    
    return True



test_board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

test_board2 = [["8","3",".",".","7","5",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

test_board3 = [[".",".","4",".",".",".","6","3","."],
               [".",".",".",".",".",".",".",".","."],
               ["5",".",".",".",".",".",".","9","."],
               [".",".",".","5","6",".",".",".","."],
               ["4",".","3",".",".",".",".",".","1"],
               [".",".",".","7",".",".",".",".","."],
               [".",".",".","5",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."]]

result1 = isValidSudoku( test_board1 )
result2 = isValidSudoku( test_board2 )

print( "Test 1 - Expected Value: True | Actual Value:", result1 )
print( "Test 2 - Expected Value: False | Actual Value:", result2 )
