#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
## Create a helper function to check if I can jump two
## If yes, move pointer 2 spaces, jumps +1
## If not, move pointer once, jumps +1
## Return jumps

#Runtime: O(n)
#Space: Constant

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c)-1:
        can_jump_two = check_two(c, i)
        if can_jump_two is True:
            i += 2
            jumps += 1
        else:
            i += 1
            jumps += 1
    return jumps

def check_two(c, i):
    if i+2 <= len(c)-1:
        if c[i+2] == 1:
            return False
        return True
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()