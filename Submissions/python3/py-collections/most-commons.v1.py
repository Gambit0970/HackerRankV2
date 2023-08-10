#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict



if __name__ == '__main__':
    s = input()
    occurs = OrderedDict()
    for l in s:
        if l in occurs:
            occurs[l]+=1
        else:
            occurs[l]=1
    m=0
    count=0
    for _ in range(3):
        m = max(occurs.values())
        for l in sorted(occurs.keys()):
            if occurs[l]==m and count<3:
                print(l,occurs[l])
                count+=1
                occurs[l]=-1
