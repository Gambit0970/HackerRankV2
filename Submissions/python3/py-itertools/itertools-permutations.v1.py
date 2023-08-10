from itertools import permutations
word, num = input().split(" ")
perms = list()
items = list(permutations(word,int(num)))
for item in items:
    perms.append("".join(x for x in item))
perms.sort()
for perm in perms:
    print(perm)
