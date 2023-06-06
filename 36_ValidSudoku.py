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
#   board is not big enough require a faster solution. We can use 
#   sets to help us identify if any duplicates exist or not.
def isValidSudoku( board ):
    # Number of rows and columns is predefined, making
    # our task much easier. Iterate through each row
    # and column, as well as square, and validate each
    # requirement of the board.
    rows = [ set( ) for x in range( 9 ) ]
    cols = [ set( ) for x in range( 9 ) ]
    squares = [ [ set( ) for x in range( 3 ) ] for y in range( 3 ) ]
    
    for y in range( 9 ):
        for x in range( 9 ):
            # Python is row-major. Get the value of the current
            # cell.
            cell_value = board[ y ][ x ]
            
            # Check if cell_value is a number, or not "."
            if cell_value == ".":
                continue
            
            # Now check if the value exists in its current row,
            # column, or square already
            if cell_value in rows[ y ]:
                return False
            if cell_value in cols[ x ]:
                return False
            # Use the floor operator to identify which square the
            # current x and y value belong to
            if cell_value in squares[ y // 3 ][ x // 3 ]:
                return False

            # This is our first time encountering the value in the
            # row, column, and square. Add it to our set.
            rows[ y ].add( cell_value )
            cols[ x ].add( cell_value )
            squares[ y // 3 ][ x // 3 ].add( cell_value )

    return True



# -------------------------------------------------------------
# TEST SUITE available below.
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
result3 = isValidSudoku( test_board3 )

print( "Test 1 - Expected Value: True | Actual Value:", result1 )
print( "Test 2 - Expected Value: False | Actual Value:", result2 )
print( "Test 3 - Expected Value: False | Actual Value:", result3 )
