# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K,M = input().split(" ")
K = int(K)
M = int(M)
N = list()
tots = list()
for i in range(K):
    nums = [int(x) for x in input().split(" ")]
    N.append([x for x in nums[1:]])
for l in product(*N):
    tots.append(sum([x**2 for x in l])%M)
print(max(tots))
