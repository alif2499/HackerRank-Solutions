#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()					# Sorts the array
    present = []				# Initializing list to help finding result
    count = 0					# Initializing variable to store steps
    if len(a)==1:				# if array has single element then return it
        return a[0]
    while(1):					# Continue the loop until result is found
        present.append(a[count])		# Append current element to (present) list
        if count == len(a)-1:			# If it is at last index, return the last element
            return a[count]
        if a[count+1] not in present:		# If next element not present in (present) list, return previous element
            return a[count]
        count += 2				# If not, then increament step counter to 2 steps forward (because we already used (current) and (current+1) element)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
