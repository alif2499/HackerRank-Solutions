#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    for i in range(1,(len(grid)-1)):			# Iterates from second row to second last row (avoid border elements)
        for j in range(1,(len(grid)-1)):		# Iterates from second column to second last column (avoid border elements)
            if (grid[i][j]>grid[i-1][j]) and (grid[i][j]>grid[i+1][j]) and (grid[i][j]>grid[i][j-1]) and (grid[i][j]>grid[i][j+1]): 	# Checks left,right,up down values
                        grid[i] = grid[i][:j] + "X" + grid[i][j+1:]	# Replaces current value with "X"
                        # grid[i] = grid[i].replace(grid[i][j], "X")  	# Replaces all occurences of the substring
                        
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
