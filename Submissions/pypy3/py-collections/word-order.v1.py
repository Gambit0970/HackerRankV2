n = int(input())
a = [input() for _ in range(n)]
count = {}
for i in a:
    count[i] = count.get(i, 0) + 1
print(len(count))
print(' '.join(str(i) for i in count.values()))
