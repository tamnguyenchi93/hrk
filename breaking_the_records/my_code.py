#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    breaking = [0, 0]
    for score in scores:
        if min_score < score:
            breaking[0] += 1
            min_score = score
        if max_score > score:
            breaking[1] += 1
            max_score = score
    return breaking

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
