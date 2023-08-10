Super = set([int(x) for x in input().split()])
Strict = True
sets = int(input())
for i in range(sets):
    mini = set([int(x) for x in input().split()])
    if not(mini.issubset(Super)): Strict = False
print(Strict)
