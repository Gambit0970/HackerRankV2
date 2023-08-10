import re
for _ in range(int(input())):
    l = re.sub("(?<=\s)\&{2}(?=\s)","and",input())
    l = re.sub("(?<=\s)\|{2}(?=\s)","or",l)
    print(l)
