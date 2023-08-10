from itertools import combinations
#x = input()
#print(x)
S, k = input().split()
k = int(k)
S = sorted(S)
for i in range(1,k+1):
    for combo in list(combinations(S,i)):
        print("".join(x for x in combo))
