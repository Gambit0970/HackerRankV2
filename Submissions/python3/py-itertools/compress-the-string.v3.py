from itertools import groupby
stringI = input()
x = [list(g) for k, g in groupby(stringI)]
print(" ".join([f"({len(i)}, {i[0]})" for i in x]))
