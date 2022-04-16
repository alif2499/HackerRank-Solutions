#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Write your code here
    diff = abs(bc-wc)                         # Calculates the difference between "bc" and "wc"
    if diff <= z:                             # Checks if we need to use the "z" value (only if the difference is greater than "z")
        return ((b*bc)+(w*wc))                # If difference <= "z":-> returns the price by multiplying each amount with it's own unit price
    else:
        if bc > wc:                           # Otherwise, checks which unit price needs to be updated (replce the greater unit price with (lower unit price + "z"))
            return ((w*wc)+(b*(wc+z)))
        else:
            return ((b*bc)+(w*(bc+z)))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
