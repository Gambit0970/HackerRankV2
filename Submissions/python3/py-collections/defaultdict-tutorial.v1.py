A = []
B = []

n,m = [int(x) for x in input().split()]
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())

for item in B:
    if item in  A:
        print(" ".join([str(pos+1) for pos,val in enumerate(A) if val==item]))
    else:
        print(-1)
