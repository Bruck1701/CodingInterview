#!/bin/python3
#source : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


import math
import os
import random
import re
import sys
from collections import Counter


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)




# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    hmap = Counter(ar)
    ar = list(set(ar))
    ar.sort()
    count = 0
    
    #print(hmap, ar)
    print(ar)

    for key,value in hmap.items():
        if value>=2 and (2*key)%k==0:
            count+=int(nCr(value,2))
    
        
    for i in range(0,len(ar)-1):
        for j in range(i+1,len(ar)):
            
            if (ar[i]+ar[j])%k ==0 :
                
                count+=hmap[ar[i]]*hmap[ar[j]]
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
