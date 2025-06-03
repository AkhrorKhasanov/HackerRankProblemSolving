#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    if t.startswith(s):
        if (len(t) - len(s)) % 2:
            return 'No'
        return 'Yes'
    n = min(len(s), len(t))
    for i in range(n):
        if s[i] != t[i]:
            break
    c = len(s) + len(t) - 2 * i
    if c <= k:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()