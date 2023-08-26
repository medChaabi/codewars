# DESCRIPTION:
# Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

# You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

# Your task is to return a four-digit string that encodes that time in 24-hour time.

# Notes
# By convention, noon is 12:00 pm, and midnight is 12:00 am.
# On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015.



# Input	Output
# 8,30,am	0830
# 8,30,pm	2030
# 1,0,am	0100
# 1,0,pm	1300


# Algorithm
# 1. Convert the input time to 24-hour time.
# 2. Return the converted time.

def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    isam='am'
    if len(str(minute)) == 1:
            minute = '0' + str(minute)
    if period == isam:
        if len(str(hour)) == 1:
                hour = '0' + str(hour)
        if hour == 12:
            return f'00{str(minute)}'
        else:
            return f'{str(hour)}{str(minute)}'
    else:#pm
        moon = 12
        if hour == moon:
            return f'12{str(minute)}'
        else:
            return f'{str(moon+hour)}{str(minute)}'
        

# print(to24hourtime(8, 30, 'am'))
print(to24hourtime(8, 30, 'pm'))
# print(to24hourtime(1, 0, 'am'))
print(to24hourtime(9, 60, 'pm'))
# print(to24hourtime(12, 0, 'am'))