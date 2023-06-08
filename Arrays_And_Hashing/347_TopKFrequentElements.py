# LeetCode Problem 347: Top K Frequent Elements
# Given an integer array nums and an integer k,
# return the k most frequent elements.
# It is guaranteed that the answer is unique.

# -------------------------------------------------------------
# SOLUTION 1: Counter
#   Counter is ideally well suited for this task, as it is 
#   designed to count the number of each element in the array.
#   We can use the most_common( ) method to return our desired
#   values.
#   Presumably Counter takes O( n ) time to be created, and 
#   most_common likely takes O( n ) time, thus making our overall
#   runtime O( n ).

from collections import Counter

def topKFrequent( nums, k ):
    # Create Counter object to count each value in nums 
    c = Counter( nums )
    # Select k most common values. Use the top k values 
    # returned by the most_common( ) method of Counter.
    most_common = [ key for key, val in c.most_common( k ) ]
    
    return most_common

# -------------------------------------------------------------
# TEST SUITE available below.
nums1 = [1,1,1,2,2,3]
k1 = 2
result1 = topKFrequent( nums1, k1 )

# Visually confirm results for expected output
print( 'Results: ' )
print( 'result1:', result1 )
    
    
    