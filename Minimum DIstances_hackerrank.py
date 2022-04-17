#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    dist = []                           # Initializing list to store distances
    for i in range(len(a)):             # Iterate over each value of the array
        for j in range(i+1,len(a)):     # Iterate from next value to compare
            if a[i]==a[j]:              # Checks if equal
                dist.append(j-i)        # If yes, store the difference
                break                   # Break loop for this element
    if len(dist)==0:                    # If no distance present then return -1
        return -1
    else:
        return min(dist)                # If present, return the minimum distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
