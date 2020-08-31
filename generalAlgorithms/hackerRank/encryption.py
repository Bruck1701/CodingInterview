#!/bin/python3
# source : https://www.hackerrank.com/challenges/encryption/problem
import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l = len(s)
    row = math.floor(math.sqrt(l))
    col = math.ceil(math.sqrt(l))

    if row * col < l:
        row+=1
    
    #print(row)
    #print(col)
    
    result=[]
    for i in range(col):
        for j in range(row):
            try:
                #print(i,j)
                result.append(s[i+ (j*col)  ])
            except:
                result.append(' ')
        
        result.append(' ')
    
    tmp_string = ''.join(result)
    tmp_string = re.sub(' +', ' ', tmp_string)

    return tmp_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
