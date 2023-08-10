import re
for _ in range(int(input())):
    if re.match(r'^[789][0-9]{9}$',input()) == None:
        print("NO")
    else:
        print("YES")
