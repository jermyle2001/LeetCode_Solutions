# LeetCode Problem 1: Two Sum
# Given an array of integers nums and an integer
# target, return indices of the two numbers such
# that they add up to target.
# You may assume that each input would have 
# *exactly one solution* and you may not use
# the same element twice.

# -------------------------------------------------------------
# SOLUTION 1: Brute Force
#   Iterate through the list and add elements until the sum is
#   met. 
#   This solution takes O( n^2 ) time, as we are iterating through
#   each element n times.
def twoSum( nums, target ):
    for i in range( len( nums ) ):
        for j in range( i + 1, len( nums ) ):
            if nums[ i ] + nums[ j ] == target:
                return[ i, j ]
    
# -------------------------------------------------------------
# TEST SUITE available below.
nums1 = [ 2, 7, 11, 15 ]
target1 = 9
nums2 = [ 3, 2, 4 ]
target2 = 6
nums3 = [ 3, 3 ]
target3 = 6

result1 = twoSum( nums1, target1 )
result2 = twoSum( nums2, target2 )
result3 = twoSum( nums3, target3 )

print( 'Results:' )
print( 'result1:', result1, '| result2:', result2, '| result3:', result3 )
if result1 != [ 0, 1 ]:
    print( 'result1 failed!' )
else:
    print( 'result1 passed.' )
if result2 != [ 1, 2 ]:
    print( 'result2 failed!' )
else:
    print( 'result2 passed.' )
if result3 != [ 0, 1 ]:
    print( 'result3 failed!' )
else:
    print( 'result3 passed.' )
