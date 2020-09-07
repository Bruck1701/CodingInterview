#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.

def alternatingCharacters(s):
    
    count = 0
    key = {"A":False, "B":False }

    for el in s:
        if el == "A" and key["A"]:
            count+=1
            
        elif el=="A" and not key["A"]:
            key["A"]=True
            key["B"] = False

        elif el == "B" and key["B"]:
            count+=1
            key["A"] = False
        
        elif el == "B" and not key["B"]:
            key["B"] = True
            key["A"] = False
    
    #print(count)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()


alternatingCharacters("AAAA")
alternatingCharacters("BBBBB")
alternatingCharacters("ABABABAB")
alternatingCharacters("BABABA")
alternatingCharacters("AAABBB")

        

