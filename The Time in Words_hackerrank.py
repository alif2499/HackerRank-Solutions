#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    hours = ["one","two","three","four","five","six","seven","eight",		# Initializing array with word values against needed numbers
                "nine","ten","eleven","twelve","thirteen","fourteen",
                "fifteen","sixteen","seventeen","eighteen","nineteen",
                "twenty"]							
    if m == 0:							# From here each "if" condition is written for different variations of given conditions
        return hours[h-1]+" o' clock"
    if m == 1:
        return hours[m-1]+ " minute past "+hours[h-1]
    if m == 15:
        return "quarter past "+hours[h-1]
    if m == 30:
        return "half past "+hours[h-1]
    if m<=20:
        return hours[m-1]+" minutes past "+hours[h-1]
    if 20<m<30:
        s = str(m)
        return hours[(int(s[0])*10)-1]+" "+hours[int(s[1])-1]+" minutes past "+hours[h-1]
    if 30<m<40:
        m = 60-m
        s = str(m)
        return hours[(int(s[0])*10)-1]+" "+hours[int(s[1])-1]+" minutes to "+hours[h]
    if m == 45:
        return "quarter to "+hours[h]
    if m>=40:
        m = 60-m
        return hours[m-1]+" minutes to "+hours[h]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
