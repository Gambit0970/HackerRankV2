import numpy

N,M,P = numpy.array([int(x) for x in input().split()])

n = numpy.array([[int(x) for x in input().split()] for _ in range(N)])
m = numpy.array([[int(x) for x in input().split()] for _ in range(M)])
p = numpy.concatenate((n,m))

print(p)
