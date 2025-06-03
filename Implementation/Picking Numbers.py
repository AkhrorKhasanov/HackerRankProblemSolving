#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    maks = c = 0
    if a.count(a[0]) == len(a):
        return len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j] - a[i] in [0, 1]:
                c += 1
            else:
                if maks < c:
                    maks = c
                c = 0
    if c > maks:
        maks = c
    return maks
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
