import re
pat1 = r'(.)(?=.*\1)'
pat2 = r'[A-Z]'
pat3 = r'[0-9]'
pat4 = r'[a-zA-Z0-9]'
strIn = "B1CDB02354"
N = int(input())
for n in range(N):
    strIn = input()
    if len(re.findall(pat1, strIn)) == 0 and len(re.findall(pat2, strIn))>1 and len(re.findall(pat3, strIn))>2 and len(re.findall(pat4, strIn))==10:
        print(f"Valid")
    else:
        print(f"Invalid")
    #matches = re.findall(pat1, strIn)
    #uCase = re.findall(pat2, strIn)
    #nums =  re.findall(pat3, strIn)
    #chars = re.findall(pat4, strIn)
    #print(matches)
    #print(uCase)
    #print(nums)
    #print(chars)
