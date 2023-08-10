import numpy as np
np.set_printoptions(legacy='1.13')
arr=[int(x) for x in input().split()]
if len(arr)<3:
    print (np.eye(arr[0],arr[1],k=0))
else:
    print (np.eye(arr[0],arr[1],k=arr[2]))
