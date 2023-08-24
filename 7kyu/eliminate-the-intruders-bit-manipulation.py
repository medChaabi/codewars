# DESCRIPTION:
# Task
# You are given a string representing a number in binary. Your task is to delete all the unset bits in this
#string and return the corresponding number (after keeping only the '1's).

# In practice, you should implement this function:

# def eliminate_unset_bits(number):
# Examples
# eliminate_unset_bits("11111111") ->  255 (= 11111111)
# eliminate_unset_bits("111") ->  7
# eliminate_unset_bits("1000000") -> 1
# eliminate_unset_bits("000") -> 0


# Algorithm:
    #Method 1:
        #1. delete all unset bit (from string)
        #2. return the corresponding number (convert from binary to decimal)

def decimal_value(binary_num:int, power:int)->int:
    # print(f"{delete_unset[i]}*(2^{i})") # formula
    return int(binary_num) * (2**int(power))

def eliminate_unset_bits(number):
    # 1 
    delete_unset = list(number.replace("0",""))
    # 2
    corres_number =0
    for i in range(len(delete_unset)):
        corres_number += decimal_value(delete_unset[i],i)
    return corres_number

# print(eliminate_unset_bits("11010101010101"))
