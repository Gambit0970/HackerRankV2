from collections import OrderedDict
bought = OrderedDict()
cost = OrderedDict()
N = int(input())
for n in range(N):
    info = input().split()
    thing = ' '.join(info[:-1])
    price = int(info[-1])
    if thing in bought.keys():
        bought[thing]+=1
    else:
        bought[thing]=1
        cost[thing]=price

for i in bought.keys():
    print(f"{i} {bought[i]*cost[i]}")
