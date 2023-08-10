import numpy as np
N,M = [int(x) for x in input().split()]
arr = np.array([[int(x) for x in input().split()] for _ in range(N)],int)
print(np.transpose(arr))
print(arr.flatten())
