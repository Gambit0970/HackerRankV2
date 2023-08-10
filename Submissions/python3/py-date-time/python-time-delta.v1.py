#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    tsformat = "%a %d %b %Y %H:%M:%S %z"
    #ts1 = datetime.strptime(t1, tsformat)
    #ts2 = datetime.strptime(t2, tsformat)
    return str(int(abs(datetime.strptime(t1, tsformat)-datetime.strptime(t2, tsformat)).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
