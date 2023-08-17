# DESCRIPTION:
# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

# The order of the sequence has to stay the same.

# Examples:

# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]

# Algorithm:
    # Method 1:
        # 1. create a array1
        # 2. iterate through the given array
        # 3. check if the element is already in the array1
        # 4. if it is not in the array1, then append it to the array1 iterate through the given array
    # Method 2: 
        # for optimization i find this solution.


# Method 1:
# time complexity: O(n^2)
def distinct(seq):
    array1 = list()
    for i in seq:## O(n) in time complexity
        if i not in array1: # O(n) in time complexity
            array1.append(i)
    return array1

# Method 2:
# time complexity: O(n)
def distinct(seq):
    array1 = list()
    seen = set()
    for i in seq: ## O(n) in time complexity
        if i not in seen: # O(1) in time complexity
            array1.append(i)
            seen.add(i)
    return array1
    
