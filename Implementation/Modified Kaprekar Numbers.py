#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    lst = []
    for i in range(p, q + 1):
        s = str(i ** 2)
        d = len(str(i))
        r = int(s[-d:])
        if s[:-d]:
            l = int(s[:-d])
        else:
            l = 0
        if l + r == i:
            lst.append(i)
    if not lst:
        print('INVALID RANGE')
    print(*lst)

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
