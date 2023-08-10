import re
T = int(input())
for t in range(T):
    print(bool(re.search(r'^[+-]?\d*\.\d+$', input())))
