from collections import namedtuple
total = 0
N = int(input())
HDRs = [_.upper() for _ in input().split()]
case = namedtuple('case',HDRs)
for i in range(N):
    xyz=case(*input().split())
    total+=int(xyz.MARKS)
print(total/N)
