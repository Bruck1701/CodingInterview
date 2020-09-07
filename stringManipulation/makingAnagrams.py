#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.

def makeAnagram(a, b):
    
    hash_a = dict(Counter(a))
    hash_b = dict(Counter(b))

    union_hash = {**hash_a,**hash_b}
    count = 0

    for key, value in union_hash.items():
        if key not in hash_b:
            count+=hash_a[key]

        elif key not in hash_a:
            count+=hash_b[key]

        else:
            count+= abs(hash_a[key]-hash_b[key])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
