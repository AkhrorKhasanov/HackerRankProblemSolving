#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(n):
    flag = False
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        flag = True
    if n < 1918:
        return f"{12 if n % 4 == 0 else 13}.09.{n}"
    if n == 1918:
        return "26.09.1918"
    if flag:
        return ('12.09.' + str(n))
    else:
        return ('13.09.' + str(n))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
