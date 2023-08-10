import numpy
N,M = input().split(" ")
N = int(N)
M = int(M)
inList = list()
for i in range(N):
    inList.append([int(x) for x in input().split(" ")])

my_array = numpy.array(inList)
sum_array = numpy.sum(my_array, axis = 0)
#print(sum_array)
#print(numpy.prod(my_array, axis = 0))            #Output : [3 8]
#print(numpy.prod(my_array, axis = 1))            #Output : [ 2 12]
#print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(sum_array))                      #Output : 24
#print(my_array)

