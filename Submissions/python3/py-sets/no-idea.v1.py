n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}
AinArr = [value for value in arr if value in A]
BinArr = [value for value in arr if value in B]

print(len(AinArr)-len(BinArr))
