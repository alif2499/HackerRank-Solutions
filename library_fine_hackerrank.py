#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    #fine = 0
    if d1==1 and d2==31 and m1==1 and m2==12 and y1-y2==1:
        return 10000
    elif (d1+(m1*30.5)+(y1*365))<(d2+(m2*30.5)+(y2*365)):
        return 0
    elif (d1+(m1*30.5)+(y1*365))-(d2+(m2*30.5)+(y2*365)) <= 30:
        return 15 * (d1-d2)
    elif 365> (d1+(m1*30.5)+(y1*365))-(d2+(m2*30.5)+(y2*365)) > 30:
        return 500 * (m1-m2)
    elif (d1+(m1*30.5)+(y1*365))-(d2+(m2*30.5)+(y2*365)) >= 365:
        return 10000
    '''if y1<y2:
        return fine
    elif y1 == y2 and m1<m2:
        return fine
    elif y1 == y2 and m1==m2 and d1<=d2:
        return fine
    elif y1 == y2 and m1>=m2 and d1>:'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
