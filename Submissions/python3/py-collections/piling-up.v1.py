from collections import deque
N = int(input())

for n in range(N):
    size = int(input())
    blocks = deque([int(_) for _ in input().split()])
    m = max(blocks)
    poss = True
    while poss and len(blocks)>0:
        if blocks[0]>=blocks[-1] and blocks[0]<=m:
            m=blocks.popleft()
        elif blocks[-1]>=blocks[0] and blocks[-1]<=m:
            m=blocks.pop()
        else:
            poss=False
    if poss:
        print("Yes")
    else:
        print("No")
