#!/bin/python3

import math
import os
import random
import re
import sys


##MY SOLUTION##
# Keep a switch to let me know when I am currently in a valley
# As soon as I exit the valley, switch is false, and if I fall below sea level again, flip back to true
# Runtime: O(n)
# Space: Constant

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_altitude = 0
    num_valleys = 0
    valley = False
    for char in s:
        if char == "D":
            current_altitude -= 1
        elif char == "U":
            current_altitude += 1
        
        if current_altitude < 0 and valley is False:
            valley = True
            num_valleys += 1
        
        elif current_altitude == 0 and valley is True:
            valley = False

    return num_valleys
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()