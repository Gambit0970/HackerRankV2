import numpy
N = int(input())
print(round(numpy.linalg.det([[float(_) for _ in input().split()] for n in range(N)]),2))
