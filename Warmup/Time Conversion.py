#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    h = int(s[:2])
    f = s[-2:]
    if f == 'AM':
        h = '0' * (2 - len(str(h % 12))) + str(h % 12)
    else:
        h = '0' * (2 - len(str((h + 12) % 24))) + str((h + 12) % 24)
    if f == 'PM' and s[:2] == '12':
        return s[:-2]
    res = h + s[2:-2]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
