#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#


def stones(n, a, b):
    l = []				# Initializing empty list to store all last stone's value
    steps = n-1				# Number of steps taken will be 1 less than total number of stones
    if (a!= b):				# If the two differences are not equal
        l.append(steps*a)		# One last stone's value will be steps*a
        l.append(steps*b)		# Another last stone's value will be steps*b
        low = 1				# For finding last stone's value for the combinations of a & b
        high = steps - low		# For finding last stone's value for the combinations of a & b
        while(low<=n-2):                # For rest of the last stone's value (n-2)
            summ = (low*a)+(high*b)
            l.append(summ)
            low += 1
            high -= 1
    else:				# If the two differences are equal 
        l.append(steps*a)		# There will be single last stone's value
        return l
    
    return sorted(l)			# Return sorted list in ascending order
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
