# DESCRIPTION:
# Create a method that takes as input a name, city, and state to welcome a person. 
# Note that name will be an array consisting of one or more values that should be joined together with one space between each, 
# and the length of the name array in test cases will vary.

# Example:
# ['John', 'Smith'], 'Phoenix', 'Arizona'
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

#Algorithm
    # Method 1: 
        # prob 1: make the full name , i make this by join to string at possition
        # return the full sentence.
    # Method 2: use join built in function
        
#Method 1:
# time complexity: O(1)
def to_welcome(name,city,state):
    name = name[0]+' '+name[1]
    return f'Hello, {name}! welcome to {city}, {state}!'

print(to_welcome(['John', 'Smith'], 'Phoenix', 'Arizona'))
