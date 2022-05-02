#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.


# Below code pass all test cases but gets "Time Limit Exceeded" error------------------->

# def strangeCounter(t):
#     # Write your code here
#     j = 2
#     counter = start = 3
#     for i in range(1,t+1):
#         if i == t:
#             return counter
#         counter -= 1
#         if counter == 0:
#             counter = start*j
#             start = counter

# This is the optimized code which will pass all the test cases

def strangeCounter(t):
    counter = 0                                                 # Initialize counter variable to store the values at a particular time
    i = -1                                                      # Initializing variable to store power value
    while((counter-2)<=t):                                      # Iterate until value is less than or equal to input "t"
        i += 1                                                  # Increase the value of i (power) by 1
        counter = 3 * pow(2,i)                                  # Find the starting value of the required column where given timeframe (t) resides
    i -= 1                                                      # Decrease i by 1 because at the end of while loop i will have value 1 more than required
    counter = 3*pow(2,i)                                        # Find the starting value of the required column with desired value of i
    startTime = counter - 2                                     # Starting time frame of each column will be always 2 less than starting value for this problem
    result = counter - (t-startTime)                            # The difference between starting timeframe and t will be equal to difference between starting value and required value at desired timeframe (t)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
