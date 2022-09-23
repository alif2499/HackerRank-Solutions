#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q


def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar = []						# Initializing variable to store kaprekar numbers
    for n in range(p,q+1):					# Iterating through each element in a given range to check if kaprekar number
        if n==1 or n==0:					# Default kaprekar numbers
            kaprekar.append(n)
            continue						
        if n<=3 and n!=1:
            continue						# Skip to next iteration
        Nlength = len(str(n))					# Stores length of the number
        sqrNstring = str(n*n)					# Stores square of the number
        sqrNlength = len(sqrNstring)				# Stores length of the square
        right = sqrNstring[-Nlength:]				# Slices digits equal to original length (of n) from last
        left = sqrNstring[:(sqrNlength-Nlength)]		# Slices rest of the digits 
        if (int(left)+int(right)) == n:				# Check if sum of int value of (left) and (right) equals to original value (n)
            kaprekar.append(n)					# If yes then append to (kaprekar) list
    if len(kaprekar):						# Check if (kaprekar) list has values
        print(*kaprekar)					# If yes, then print values in one line with space separation
    else:
        print("INVALID RANGE")					#If no, then print (INVALID RANGE)

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
