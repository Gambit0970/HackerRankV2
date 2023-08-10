M = int(input())
a = {int(x) for x in input().split()}
N = int(input())
b = {int(x) for x in input().split()}
for i in sorted(a.difference(b).union(b.difference(a))):
    print(i)
