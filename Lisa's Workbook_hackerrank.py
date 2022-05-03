#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    count = 0					# Initializing variable to store no. of desired problems
    pageIndex = 1				# Initializing variable with current page no.
    for i in range(n):				# Iterating through all chapters
        for j in range(1,arr[i]+1):		# Iterating through all problems of each chapter
            if pageIndex == j:			# Checks if current page no. equals to current problem no.(j)
                count += 1			# If yes, then increament the (counter) variable
            if j%k == 0:			# Check if current problem no. equals to minimum problem no. in a page
                pageIndex += 1			# If yes, then go to next page
        if (arr[i]%k)!=0:			# After checking for each problems of a chapter, check if the problem amount is a multiple of minimum problem no. in a page
            pageIndex += 1			# If not, then go to next page. Because, without this we will be assigning problems from next chapter to current page.
    return count
                        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
