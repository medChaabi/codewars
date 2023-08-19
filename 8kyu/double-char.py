# DESCRIPTION:
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Good Luck!

# algo:
    # Method 1:
        #1. create result =>
        #1. loop for each char => char*2
        #3. save in result =/
        #4. return result
    # Method 2:
        # use list and join

#Method 1:
def double_char(input):
    result = ""
    for char in input:
        result+=char*2
    return result

#Method 2:
def double_char2(input):
    return ''.join([char*2 for char in input])
