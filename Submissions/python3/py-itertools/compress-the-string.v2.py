from itertools import groupby
x = [list(g) for k, g in groupby(input())]
print(" ".join([f"({len(i)}, {i[0]})" for i in x]))
