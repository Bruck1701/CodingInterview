#!/bin/python3
#source : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem



import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]

    min_counter = 0
    max_counter = 0

    for score in scores[1:]:
        if score < min_score:
            min_score=score
            min_counter+=1
        elif score > max_score:
            max_score = score
            max_counter+=1
    
    return max_counter,min_counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
