# LeetCode Problem 20: Valid Parentheses
# Given a string s containing just the
# characters '(', ')', '{', '}', '[', ']',
# determine if the input string is valid.
# An input string is valid if:
# - Open brakctes must be closed by the same
#   type of brackets
# - Open brackets muts be closed in the correct
#   order
# - Every close bracket has a corresponding open
#   bracket of the same time

# -------------------------------------------------------------
# SOLUTION 1: Stack pushing and popping (Brute Force)
# We will use the stack datatype to push and pop
# accordingly. We will push open parentheses, and 
# pop them when we see a closing one. If we see
# a closing one that does not match the top of
# the stack, then the string is not valid.
from collections import deque

# Utilize the deque structure for quicker append
# and pop operations, in O( 1 ) time compared to 
# O( n ) for lists
def isValid( s ):
    # Create stack data structure so that we can 
    # push and pop as needed
    stack = deque( )
    
    # For each element in p, check if open or close
    # bracket. If close bracket, check if element at 
    # the top of stack matches. If not, then return
    # False - otherwise, continue until we have nothing
    # left.
    for p in s:
        if p == '(' or p == '{' or p == '[':
            stack.append( p )
        else:
            # Check if stack is empty. If so, string is
            # invalid and return False.
            if len( stack ) <= 0:
                return False
            
            # Check if close bracket corresponds to open
            # element at top of stack. If not, return 
            # False. Otherwise, pop off stack.
            if p == ')' and stack[ -1 ] != '(':
                return False
            elif p == '}' and stack[ -1 ] != '{':
                return False
            elif p == ']' and stack[ -1 ] != '[':
                return False
            else: 
                stack.pop( )
    
    # If there are any elements left on the stack, then
    # our string is also invalid.
    if len( stack ) != 0:
        return False
    
    # Return True otherwise.
    return True

# -------------------------------------------------------------
# TEST SUITE available below.
# Visually confirm results are correct!
test_input1 = "()"
test_input2 = "()[]{}"
test_input3 = "(]"

result1 = isValid( test_input1 )
result2 = isValid( test_input2 )
result3 = isValid( test_input3 )

print( "Test 1 - Expected Value: True | Actual Value:", result1 )
print( "Test 2 - Expected Value: True | Actual Value:", result2 )
print( "Test 3 - Expected Value: False | Actual Value:", result3 )