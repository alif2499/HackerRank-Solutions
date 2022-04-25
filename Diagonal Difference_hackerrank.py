#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    LtoRsum = 0				# Initialize variable to store LeftToRight diagonal sum
    RtoLsum = 0				# Initialize variable to store RightToLeft diagonal sum
    j = len(arr)-1			# Initialize variable with last element index
    for i in range(len(arr)):		# Iterate over each row to get LeftToRight diagonal sum
        LtoRsum += arr[i][i]
    for i in range(len(arr)):		# Iterate over each row to get RightToLeft diagonal sum
        RtoLsum += arr[i][j]
        j -= 1				
    return abs(LtoRsum-RtoLsum)		# returns the absolute value
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
