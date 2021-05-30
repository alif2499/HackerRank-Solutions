#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maximumStones(arr):
    # Write your code here
    odd = 0
    even = 0
    arrLength = len(arr)
    for i in range(0,arrLength):
        if i%2==0:
            odd += arr[i]
        else:
            even += arr[i]
    minimum = min(even,odd)
    return 2*minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
