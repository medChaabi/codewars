# DESCRIPTION:
# Input: Array of elements

# ["h","o","l","a"]

# Output: String with comma delimited elements of the array in th same order.

# "h,o,l,a"

# Note: if this seems too simple for you try the next level


def print_array(arr):
    return ",".join(str(x) for x in arr)

# print(print_array(["h","o","l","a"]))
# print(print_array([2,3,4,5]))