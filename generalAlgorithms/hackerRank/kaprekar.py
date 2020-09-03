
# source: https://www.hackerrank.com/challenges/kaprekar-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    found=False
    result=[]
    for num in range(p,q+1):
        
        res = num*num
        st = str(res)
        if len(st)<2:
            num1=0
            num2=res
        else:
        
            num1 = int(st[0:len(st)//2])
            num2 = int(st[len(st)//2:])
        if num1+num2 == num:
            found=True
            result.append(str(num))

    if (found==False):
        print("INVALID RANGE")
    else:
        print(" ".join(result))


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
