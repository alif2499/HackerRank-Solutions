#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr


def beautifulTriplets(d, arr):
    # Write your code here
    count = 0					# Initializing (count) variable to store the number of beautiful triplets
    for i in range(len(arr)):			# For iterating through each element
        sum2 = arr[i]+d				# Storing second value of triplet for comparison
        sum3 = sum2+d				# Storing third value of triplet for comparison
        if (sum2 in arr) and (sum3 in arr):	# Check if the two values except the first one (arr[i]) is present in the array
            count += 1				# If yes then increase count variable by 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
