#!/bin/python3

import math
import os
import random
import re
import sys

''' This "flatlandSpaceStations" function passes all test cases except for
    test case 14 and 15. It generates runtime error in those two cases.
    This bug will be fixed shortly.'''

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    nearestStation = []						# Initializing list to store distance to nearest station for each node
    for i in range(n):						# Iterating for each node
        stationDistance = []					# Initializing list to store distance to all station for each node
        for station in c:					# Iterating for each station
            stationDistance.append(abs(station-i))		# Calculating and appending distances to all station
        nearestStation.append(min(stationDistance))		# Calculating and appending distance to the nearest station
    return max(nearestStation)					# Returning the maximum value among all nearest stations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
