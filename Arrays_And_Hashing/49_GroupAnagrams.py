# LeetCode Problem 49: Group Anagrams
# Given an array of strs, gropu the anagrams together. 
# You can return the answer in any order.

# -------------------------------------------------------------
# SOLUTION 1: Dictionaries
#   Use the defaultdict datatype to categorize our strings. We 
#   will sort our strings and use those values as the keys to our
#   dictionary, adding them to each mapped element in the dictionary.
#   Sorting takes O( n * log( n ) ) time, and running through the 
#   single loop takes O( n ) time. Dictionary accesses are assumed to take
#   O( 1 ) time.
from collections import defaultdict

def groupAnagrams( strs ):
    # Create dictionary, give it 'list' datatype elements
    sorted_dict = defaultdict( list )
    # Sort each word, append to sorted element in dictionary
    for word in strs:
        # Sort current word, store as tuple so that it will 
        # fit in our datatype
        sorted_word = tuple( sorted( word ) )
        
        # Append word based on sorted version in dictionary
        sorted_dict[ sorted_word ].append( word )
    
    # Return as list of values in dictionary
    return list( sorted_dict.values( ) )

# -------------------------------------------------------------
# TEST SUITE available below.
strs1 = ["eat","tea","tan","ate","nat","bat"]
result1 = groupAnagrams( strs1 )

# Visually confirm results for expected output
print( 'Results: ' )
print( 'result1:', result1 )

