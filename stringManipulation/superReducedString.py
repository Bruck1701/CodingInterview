

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.


def superReducedString(s):
    l = [s[0]]
    for el in s[1:]:
        if len(l)>0 and el == l[-1]:
            l.pop()
        else:
            l.append(el)
    if len(l)>0:
        return  "".join(l)
    else:
        return "Empty String"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()



superReducedString("aaabccddd")

superReducedString("baab")
superReducedString("aa")
superReducedString("abccddd")

superReducedString("acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj")
superReducedString("ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx")

#superReducedString("zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh")