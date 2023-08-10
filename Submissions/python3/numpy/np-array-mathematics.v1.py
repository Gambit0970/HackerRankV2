import numpy as np
N,M = [int(x) for x in input().split()]

A = np.array([[int(x) for x in input().split()] for _ in range(N)])
B = np.array([[int(x) for x in input().split()] for _ in range(N)])

print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.array(np.divide(A,B),int))
print(np.mod(A,B))
print(np.power(A,B))



