N = int(input())
X = [int(x) for x in input().split()]
print(len([_ for _ in X if _>=0])==len(X) and any([str(_)==str(_)[::-1] for _ in X]))
