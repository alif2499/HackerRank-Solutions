#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    count = 1					# Initialize by 1, because there will be at least one word
    for i in range(len(s)):			# Iterate over each element of the string
        if s[i]<'a':				# Check if current character is uppercase
            count+=1				# If yes, increament counter
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
