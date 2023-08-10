N,X = [int(_) for _ in input().split()]
arr = [[float(i) for i in input().split()] for j in range(X)]
print(*(round(sum(y)/len(y),1) for y in list(zip(*arr))),sep="\n")
