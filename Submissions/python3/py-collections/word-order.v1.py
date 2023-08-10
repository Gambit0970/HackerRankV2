n = int(input())
wordC = {}
for i in range(n):
    word = input()
    wordC[word] = wordC.get(word,0)+1
#    if word not in wordC.keys():
#        wordC[word]=1
#    else:
#        wordC[word]+=1
print(len(wordC))
print(' '.join(str(x) for x in wordC.values()))
