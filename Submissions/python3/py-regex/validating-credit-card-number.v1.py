import re
p1 = r'([456]\d{3}-?\d{4}-?\d{4}-?\d{4})$'
p2 = r"(\d)\1{3,}"

N = int(input())
for n in range(N):
    strIn = input()
    if re.match(p1, strIn) != None:
        strIn = re.sub(r"-", "", strIn)
        if len(re.findall(p2, strIn))>0:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
