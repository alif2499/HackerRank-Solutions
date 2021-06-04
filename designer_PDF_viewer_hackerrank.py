#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

####### Function statrts here
def designerPdfViewer(h, word):
    # Write your code here
    length = len(word)
    arr = []
    for i in word:
        index = string.ascii_lowercase.index(i)
        arr.append(h[index])
    return length*max(arr)

####### Function ends here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
