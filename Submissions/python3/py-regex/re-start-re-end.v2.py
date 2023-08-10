s = input()
f = input()
found = False
for i in range(len(s)-len(f)+1):
    if s[i:i+len(f)] == f:
        print(f"({i}, {i+len(f)-1})")
        found = True
if not found:
    print("(-1, -1)")
