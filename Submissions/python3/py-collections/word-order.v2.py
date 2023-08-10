n = int(input())
wordC = {}
for i in range(n):
    word = input()
    if word not in wordC.keys():
        wordC[word]=1
    else:
        wordC[word]+=1
print(len(wordC))
print(' '.join(str(x) for x in wordC.values()))
