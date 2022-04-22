#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.


def countingSort(arr):
    # Write your code here
    result = [0]*100				# Initializes array of 100 zeros
    for i in range(len(arr)):			# Iterate over each element of the array
        result[arr[i]] += 1			# Increament the value of each position according to the respective positional value from given array
    							# Here the result array is used as counter to the occurence of elements in given array
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
