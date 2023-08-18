# DESCRIPTION:
# Create a method that takes as input a name, city, and state to welcome a person. 
# Note that name will be an array consisting of one or more values that should be joined together with one space between each, 
# and the length of the name array in test cases will vary.

# Example:
# ['John', 'Smith'], 'Phoenix', 'Arizona'
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

#Algorithm
    
#Method 1:
# time complexity: O(n)
def say_hello(name,city,state):
    # 1. join the (name) list by space
    str_name = ' '.join(name) # O(n)
    # 2. return the string
    return f'Hello, {str_name}! Welcome to {city}, {state}!'

print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))
