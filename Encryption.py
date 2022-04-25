#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(' ', '')				# First removing all whitespaces from input string
    x = []						# Initializing list to store intermediate version of final encrypted string
    result = ""						# Initializing empty string to store final encrypted result
    rows = math.floor(math.sqrt(len(s)))		# Stores the number of rows of the intermediate version
    cols = math.ceil(math.sqrt(len(s)))			# Stores the number of columns of the intermediate version
    if (rows*cols)<len(s):				# If (rows*cols) is less than total string length, increament row by 1 to store all elements
        rows+=1

    charIndex = 0					# Initializing variable to keep track of characters
    for i in range(rows):				# Iterate through each row
        if i == (rows-1):				# If current row is last row, calculate total number of elements upto second last row
            cols = len(s)-(i*cols)			# subtract the total number from string length and assign it to (cols) variable for number of columns in last row
        y = ""						# Initialize empty string to store intermediate string at each index of (x) list
        for j in range(cols):				# Iterate through each column
            y += s[charIndex]				# Concatenate characters from beginning of the given string
            charIndex += 1				# Increament the index by 1
        x.append(y)					# Append to the (x) list at each index

    cols = math.ceil(math.sqrt(len(s)))			# Again store the number of columns of the intermediate version as it can be changed in first "for" loop
    
    for i in range(cols):				# Now iterate through each column
        if i == (len(x[-1])):				# If current column number equals to the length of last element of (x) list
            rows = rows-1				# Decreament the row number by 1
        for j in range(rows):				# Iterate for each row
            result += x[j][i]				# Concatenate current character to result string
        result += " "					# Add one whitespace after each word
    return result					# Returns the encrypted string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
