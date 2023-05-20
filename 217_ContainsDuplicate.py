# LeetCode Problem 217: Contains Duplicate
# Given an integer array nums, return true if any value 
# appears at least twice in the array, and return false 
# if every element is distinct.

# -------------------------------------------------------------
# SOLUTION 1: List and Set lengths
#   A list can contain duplicates, while a set cannot.
#   Thus if we cast our list into a set and compare the
#   size of the list and set, then we can detemrine if
#   any duplicates existed. 
#   This solution takes O( n ) time to run, as casting the
#   list into a set takes O( n ) time, and finding the length
#   of an array tkaes O( 1 ) time.
def containsDuplicateLength( nums ):
    length = len( nums )
    nums = set( nums )
    if length != len( nums ):
        return True
    else:
        return False

# -------------------------------------------------------------
# SOLUTION 2: List.count()
#   In Python, the count() method returns the number
#   of times an element repeates in a list. We can 
#   iterate through the list and use count() on each
#   element to check.
def containsDuplicateCount( nums ):
    for i in nums:
        if nums.count( i ) != 1:
            return True
    return False


# -------------------------------------------------------------
# TEST SUITE available below.
nums1 = [1, 2, 3, 4]                # No duplicates in list
nums2 = [1, 1, 2, 2, 3, 3, 4, 4]    # Duplicates in list

ResultLength1 = containsDuplicateLength( nums1 )
ResultLength2 = containsDuplicateLength( nums2 )
CountLength1 = containsDuplicateCount( nums1 )
CountLength2 = containsDuplicateCount( nums2 )

print( 'Results: ' )
print( 'ResultLength1:', ResultLength1, '| ResultLength2: ', ResultLength2 )
print( 'CountLength1:', CountLength1, '| CountLength2:', CountLength2 )

if ResultLength1 != False:
    print( 'Length1 failed!' )
else: 
    print( 'Length1 passed.' )
if ResultLength2 != True:
    print( 'Length2 failed!' )
else:
    print( 'Length2 passed.' )

if CountLength1 != False:
    print( 'CountLength1 failed!' )
else: 
    print( 'CountLength1 passed.' )
if CountLength2 != True:
    print( 'CountLength2 failed!' )
else:
    print( 'CountLength2 passed.' )
        