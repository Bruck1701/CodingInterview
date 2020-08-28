#!/bin/python3

import math
import os
import random
import re
import sys


def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(test_str):
    res = [test_str[i: j] for i in range(len(test_str)) 
            for j in range(i + 1, len(test_str) + 1)] 

    hashsum={}
    count = 0
    idxs=set()
    bag={}
    for el in res:
        value = ''.join(sorted(el))
        if value not in hashsum:
            hashsum[value]=1

        else:
            hashsum[value]+=1
            idxs.add(value)

    for el in idxs:
        count += nCr(hashsum[el],2)
    
    return count
   



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
