#!/bin/python3

# source:  https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.

def isValid(s):
    lett_occ = Counter()
    occ_map = Counter()

    for el in s:
        
        if occ_map[lett_occ[el]]>0:
            occ_map[lett_occ[el]]-=1    
        lett_occ[el]+=1
        occ_map[lett_occ[el]]+=1

    tuples_list = [(k,v) for k,v in sorted(occ_map.items(),key = lambda x:x[0]) if v!= 0 ]

    if len(tuples_list)==1:
        return "YES"
    
    if len(tuples_list)==2:
        el1 = tuples_list[0]
        el2 = tuples_list[1]
        #print("el1: ",el1,"el2:",el2)
        if (el2[0]-el1[0]==1 ) and el2[1]==1:
            return "YES"
        
        if el1[0]==1 and el1[1]==1:
            return "YES"

    #print(tuples_list)

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
