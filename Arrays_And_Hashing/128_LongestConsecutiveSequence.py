# LeetCode Problem 128: Longest Consecutive Sequence
# Given an unsorted array of integers "nums",
# return the length of the longest consecutive
# elements sequence.
# You must write an algorithm that runs in O( n ) time.

def longestConsecutive( nums ):
    # Create and place values of num into set
    nums_set = set( nums )
    
    # Loop through again, looking for consecutive
    # sequences.
    longest_length = 0
    for num in nums:
        curr_longest = 1
        i = 1
        # Find sequence to the left / less than num.
        # Use i to keep moving left.
        while num - i in nums_set:
            nums_set.remove( num - i )
            curr_longest += 1
            i += 1
            
        i = 1
        while num + i in nums_set:
            nums_set.remove( num + i )
            curr_longest += 1
            i += 1
           
        # Compare the length of the last sequence with
        # the length of the longest sequence and take
        # the longer of the two.
        longest_length = max( curr_longest, longest_length )
        
    return longest_length


# -------------------------------------------------------------
# TEST SUITE available below.
# Visually confirm results are correct!
test_arr1 = [ 100, 4, 200, 1, 3, 2 ]
test_arr2 = [ 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 ] 

result1 = longestConsecutive( test_arr1 )
result2 = longestConsecutive( test_arr2 )


print( "Test 1 - Expected Value: 4 | Actual Value:", result1 )
print( "Test 2 - Expected Value: 9 | Actual Value:", result2 )

