# LeetCode Problem 238: Product of Array Except Self
# Given an integer array 'nums', return an array 'answer'
# such that answer[ i ] is equal to the product of all the
# elements of nums except nums[ i ].
# The product of any prefix or suffix is guaranteed to fit
# in a 32-bit integer.

# You must write an algorithm that runs in O( n ) time and 
# DOES NOT use the Division operation.

# -------------------------------------------------------------
# SOLUTION 1: Total Sum
#   Create the prefixes and suffixes of each element in nums.
#   The Prefix can be defined as for a value i, the product of
#   all elements <= i. Conversely, the Suffix can be defined as 
#   the product of all elements >= i. By multiplying
#   Suffix[ i + 1 ] * Prefix[ i - 1 ] we can avoid using the 
#   Division operation and achieve our goal.

# Import array as arr. Note: array is NOT built-in and needs to
# be imported.
import array as arr

def productExceptSelf( nums ):
    # Calculate the Prefixes of num, which is the product
    # of all elements <= i.
    prefix = [ 1 ] * len( nums )
    for i in range( len( nums ) ):
        if i == 0:
            prefix[ i ] = nums[ i ]
        else:
            prefix[ i ] = prefix[ i - 1 ] * nums[ i ]
    
    # Calculate the Suffixes of num, which is the product
    # of all elements >= i
    suffix = [ 1 ] * len( nums )
    for i in reversed( range( len( nums ) ) ):
        if i == len( nums ) - 1:
            suffix[ i ] = nums[ i ]
        else:
            suffix[ i ] = suffix[ i + 1 ] * nums[ i ]

    products = arr.array( 'i' )
    for i in range( len( nums ) ):
        if i == 0:
            products.append( suffix[ i + 1 ] )
        elif i == len( nums ) - 1:
            products.append( prefix[ i - 1 ] )
        else:
            products.append( prefix[ i - 1 ] * suffix[ i + 1 ] )
            
    return products
    
    

# -------------------------------------------------------------
# TEST SUITE available below.
nums1 = [ 1, 2, 3, 4 ]
result1 = productExceptSelf( nums1 )
nums2 = [ -1, 1, 0, -3, 3 ] 
result2 = productExceptSelf( nums2 )

print( 'Results: ' )
print( 'result1:', result1, '| result2:', result2 )

if result1 != arr.array( 'i', [ 24, 12, 8, 6 ] ):
    print( 'result1 failed!' )
else:
    print( 'result1 passed.' )

if result2 != arr.array( 'i', [ 0, 0, 9, 0, 0 ] ):
    print( 'result2 failed!' )
else:
    print( 'result2 passed.' )