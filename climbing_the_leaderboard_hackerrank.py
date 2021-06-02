#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    result = []
    lengthPlayer = len(player)
    ranked = sorted(set(ranked))
    player = sorted(player)
    #return ranked, player
    lengthRanked = len(ranked)
    initial = 0
    for i in range(lengthPlayer):
        for j in range(initial,lengthRanked):
            if player[i]>ranked[j]:
                if j+1==lengthRanked:
                    result.append(1)
            elif player[i]==ranked[j]:
                result.append(lengthRanked-j)
                initial = j
                break
            else:
                result.append(lengthRanked+1-j)
                initial = j
                break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
