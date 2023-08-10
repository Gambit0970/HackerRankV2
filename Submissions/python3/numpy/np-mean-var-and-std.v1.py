import numpy
N,M = [int(_) for _ in input().split()]
my_array=numpy.array([[int(_) for _ in input().split()] for n in range(N)])
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array),11))
