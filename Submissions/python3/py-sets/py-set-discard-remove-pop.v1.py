n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    fun = input().split()
    if fun[0] == "pop":
        s.pop()
    elif fun[0] == "remove":
        try:
            s.remove(int(fun[1]))
        except Exception as e:
            print(e)
    elif fun[0] == "discard":
        s.discard(int(fun[1]))
print(sum(s))
