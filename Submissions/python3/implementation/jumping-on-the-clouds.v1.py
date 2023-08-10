#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    j = 0
    i = 0
    while i<len(c)-1:
        if i<len(c)-2:
            if c[i+2] == 0:
                print(i,"Jump to ",i+2)
                j+=1
                i+=2
            else:
                print(i,"Jump to ",i+1)
                j+=1
                i+=1
        else:
            print(i,"Jump to ",i+1)
            j+=1
            i+=1
    return j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
