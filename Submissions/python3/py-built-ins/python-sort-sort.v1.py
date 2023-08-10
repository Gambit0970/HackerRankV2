#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n,m = [int(_) for _ in input().split()]
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr.sort(key=lambda arr: arr[k])
    for i in arr:
        print(" ".join(str(_) for _ in i))
