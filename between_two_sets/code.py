#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    count = 0
    min_x = max(a)
    max_x = min(b)
    print("min_x %d, max_x %d" % (min_x, max_x))
    for i in range(min_x, max_x +1):
        a_factor = True
        b_factor = True
        for ai in a:
            if i % ai != 0:
                a_factor = False
                break
        if not a_factor:
            continue
        for bi in b:
            if bi % i != 0:
                b_factor = False
                break
        if not b_factor:
            continue
        count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
