#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    c = 0
    s = '0'
    res = 0
    for i in path:
        if i == 'U':
            c += 1
        else:
            c -= 1
        if c > 0:
            s += '+'
        elif c < 0: 
            s += '-'
        else:
            s += '0'
    return s.count('0-')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
