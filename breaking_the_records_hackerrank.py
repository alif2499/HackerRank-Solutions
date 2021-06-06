#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    score = []
    for i in scores:
        if i not in score:
            score.append(i)
    low = 999999999
    high = 0
    low_count = 0
    high_count = 0
    result = []
    length = len(score)
    for i in range(length):
        low = min(low,score[i])
        high = max(high,score[i])
        if i > 0 and low == score[i]:
            low_count += 1
        elif i > 0 and high == score[i]:
            high_count += 1
    result.append(high_count)
    result.append(low_count)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
