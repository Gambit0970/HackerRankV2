n = int(input())
for i in range(n):
    a = int(input())
    A = set(int(x) for x in input().split())
    b = int(input())
    B = set(int(x) for x in input().split())
    print(A.issubset(B))
