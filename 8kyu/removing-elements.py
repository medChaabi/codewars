# DESCRIPTION:
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!


def remove_every_other(my_list):
    result_list = []
    for i in range(0,len(my_list),2):
        result_list.append(my_list[i])
    return result_list

    
# remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"])