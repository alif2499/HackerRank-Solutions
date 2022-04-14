#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    rows = len(topic)    		# takes the length for iterating
    maximum = 0          		# Initializing maximum number of items
    team = 1             		# Initializing number of teams by 1 as atleast one team will get max items no matter the number of items
    countValue = []	 		# Initializing array to store item count for every team
    returnValue = []	 		# Initializing array to store the result
    for i in range(rows):		
        for j in range(i+1, rows):
            a = int(topic[i],2)		# Converting binary->decimal
            b = int(topic[j],2)		# Converting binary->decimal
            result = (a | b)		# Performing OR operation
            out = bin(result).replace("0b","")		# Converting decimal->binary
            count = out.count('1')	# Counting number of 1's present
            countValue.append(count)	# Storing each count for number of 1's
    maximum = max(countValue)		# Storing max count for number of 1's
    team = countValue.count(maximum)	# Storing frequency of maximum count (number of teams with maximum items) 
    returnValue.append(maximum)		# Storing maximum count in the result array
    returnValue.append(team)		# Storing number of teams with maximum topics

    return returnValue

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
