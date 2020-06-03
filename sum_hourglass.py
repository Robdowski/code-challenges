#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    highest_hourglass = float("-inf")
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr)-1):
            current_hourglass_sum = sum_hourglass(i, j, arr)

            if current_hourglass_sum > highest_hourglass:
                highest_hourglass = current_hourglass_sum
    
    return highest_hourglass


## This code is not used, however, if the hourglass were required to be complete, without 0's, this code would be used.
def check_for_hourglass(i, j, arr):
    if arr[i][j-1] != 0 or arr[i][j+1] != 0:
        return False

    if arr[i-1][j-1] == 0 or arr[i-1][j] == 0 or arr[i-1][j+1] == 0:
        return False

    if arr[i+1][j-1] == 0 or arr[i+1][j] == 0 or arr[i+1][j+1] == 0:
        return False

    return True

def sum_hourglass(i, j, arr):
    current_hourglass_sum = 0

    #TOP
    current_hourglass_sum += arr[i-1][j-1]
    current_hourglass_sum += arr[i-1][j]
    current_hourglass_sum += arr[i-1][j+1]
    #MID
    current_hourglass_sum += arr[i][j]
    #BOT
    current_hourglass_sum += arr[i+1][j-1]
    current_hourglass_sum += arr[i+1][j]
    current_hourglass_sum += arr[i+1][j+1]

    return current_hourglass_sum






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()