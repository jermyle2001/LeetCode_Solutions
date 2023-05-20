# Leetcode Problem 242: Valid Anagram
# Given two strings s and t, return true if t is an
# anagram of s, and false otherwise.

# SOLUTION 1: Sort String
#   Use the 'sorted' method provided by Python to sort
#   the strings. After sorting the strings, they can be
#   compared to find equality.
#   This takes O( n*log(n) ), as sorting takes that much
#   time, whereas comparing the strings would take O( n )
#   time.

def isAnagram( s, t ):
    print( 'Checking for anagrams' )
    s_sorted = sorted( s )
    t_sorted = sorted( t ) 
    if t_sorted == s_sorted:
        return True
    else:
        return False

# -------------------------------------------------------------
# TEST SUITE available below.
s1 = 'CCAABBEFG'    # s1 and t1 are anagrams.
t1 = 'EFGCCAABB'
s2 = 'CCAABBEFG'    # s2 and t2 are NOT anagrams.
t2 = 'EFGCCAAB'
result1 = isAnagram( s1, t1 )
result2 = isAnagram( s2, t2 )

print( 'Results: ' )
print( 'result1:', result1, '| result2: ', result2 )

if result1 != True:
    print( 'result1 failed!' )
else:
    print( 'result1 passed.' )

if result2 != False:
    print( 'result2 failed!' )
else:
    print( 'result2 passed.' )
