from itertools import *
S, k = input().split()
S = sorted(S)
k = int(k)
for x in list(combinations_with_replacement(S,k)):
    print(''.join(_ for _ in x))
