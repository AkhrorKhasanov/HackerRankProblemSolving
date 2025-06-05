#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    data = {}
    res = 0
    c = 1
    for i in arr:
        d = 1
        for j in range(i // k + 1):
            if i > d + k - 1:
                lst = [z for z in range(d, d + k)]
            else:
                lst = [z for z in range(d, i + 1)]
            if lst:
                data[c] = lst
                c += 1
            d += k
            
    for k, v in data.items():
        if k in v:
            res += 1
    # return data
    return res
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
