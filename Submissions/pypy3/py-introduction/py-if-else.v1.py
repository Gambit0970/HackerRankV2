#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    word1 = ""
    if n % 2 == 1:
        word1 = ""
    elif n < 6:
        word1 = "Not "
    elif n < 21:
        word1 = ""
    else:
        word1 = "Not "
    print(word1+"Weird")
