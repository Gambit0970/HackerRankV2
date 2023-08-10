
from itertools import product
comb = list()
for i in range(2):
    comb.append([int(x) for x in input().split(" ")])
print(" ".join(str(x)for x in list(product(*comb))))
#for x in list(product(*comb)):
#    print(str(x))
