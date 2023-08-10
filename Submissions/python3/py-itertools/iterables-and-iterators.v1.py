from itertools import combinations
K = int(input())
s = input().split()
N = int(input())
count = 0
x = list(combinations(s,N))
for i in x:
    if "a" in i:
        count+=1
print(count/len(x))
