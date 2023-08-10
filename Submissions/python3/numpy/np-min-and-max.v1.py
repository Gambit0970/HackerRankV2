import numpy as np
N,M = [int(x) for x in input().split()]
arr = np.array([[x for x in input().split()] for _ in range(N)],int)
print(np.max(np.min(arr, axis = 1)))
