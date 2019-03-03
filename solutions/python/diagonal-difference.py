#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    firstDaigonal = 0
    secondDaigonal = 0
    leftIndex = 0
    rightIndex = len(arr) - 1

    for row in arr:
        firstDaigonal+=row[leftIndex]
        secondDaigonal+=row[rightIndex]
        leftIndex+=1
        rightIndex-=1
    
    return abs(firstDaigonal - secondDaigonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

