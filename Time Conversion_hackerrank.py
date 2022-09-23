#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2]=='P' and s[:2]!="12":			# Checks if it is "PM" and not "12"
        return str(int(s[0:2])+12)+s[2:-2]		# If yes, returns the sum of 12 with current time
    elif s[-2]=='P' and s[:2]=="12":			# Checks if it is "PM" and "12"
        return s[:-2]					# If yes, returns the current time
    elif s[-2]=='A' and s[:2]=="12":			# Checks if it is "AM" and "12"
        return str(int(s[0:2])-12)+'0'+s[2:-2]		# If yes, returns the subtraction of 12 from current time
    elif s[-2]=='A' and s[:2]!="12":			# Checks if it is "AM" and not "12"
        return s[:-2]					# If yes, returns the current time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
