from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    inst = input().split()
    if inst[0] == "append":
        d.append(inst[1])
    elif inst[0] == "appendleft":
        d.appendleft(inst[1])
    elif inst[0] == "clear":
        d.clear()
    elif inst[0] == "extend":
        d.extend(inst[1])
    elif inst[0] == "extendleft":
        d.extendleft(inst[1])
    elif inst[0] == "count":
        d.count(inst[1])
    elif inst[0] == "pop":
        d.pop()
    elif inst[0] == "popleft":
        d.popleft()
    elif inst[0] == "remove":
        d.remove(inst[1])
    elif inst[0] == "rotate":
        d.rotate(int(inst[1]))
    else:
        print(f"{inst} unknown")
print (' '.join(x for x in d))
