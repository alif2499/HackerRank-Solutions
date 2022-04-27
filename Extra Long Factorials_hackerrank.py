#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if n == 1:						# Terminating condition for reccursive function
        return 1
    factorial = n*extraLongFactorials(n-1)		# Keep recurring until meets the terminating condition
    return factorial

if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
