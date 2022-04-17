#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count = 0						# Initializing variable to store number of games
    currentPrice = 0					# Initializing variable to store money left after each purchase
    if s>p:						# Check if the available money is enough to buy the first game
        currentPrice = s-p				# If yes, reduce money by the amount of first game price
        count+=1					# Increament number of games bought
    while (p-d)>=m and currentPrice>=(p-d):		# Check if next game price is greater or equal to min price and current price is enough to buy
        p-=d						# updates the next game price
        count += 1					# Increament number of games bought
        currentPrice -=p				# Updates the available money after each purchase
    if (p-d)<m:						# Check if next game price is less than min price
        count = count + (currentPrice//m)		# If yes, purchase games with available money at min price and update counter
    return count
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
