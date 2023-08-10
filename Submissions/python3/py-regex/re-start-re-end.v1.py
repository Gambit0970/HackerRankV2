#s = input()
#f = input()
#found = False
#for i in range(len(s)-len(f)+1):
#    if s[i:i+len(f)] == f:
#        print(f"({i}, {i+len(f)-1})")
#        found = True
#if not found:
#    print("(-1, -1)")

    
import re
s = input()
f = input()
m = re.finditer(r'(?=('+f+'))', s)
if re.search(r'(?=('+f+'))', s):
    print("\n".join(f"({_.start()}, {_.start()+len(f)-1})" for _ in m))
else:
    print("(-1, -1)")
