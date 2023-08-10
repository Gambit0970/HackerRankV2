from math import atan, degrees
degree_sign = u'\N{DEGREE SIGN}'
AB = float(input())
BC = float(input())
#AC = sqrt(AB**2 + BC**2)

#print(AB)
#print(BC)
#print(AC)
print(f"{round(degrees(atan(AB/BC)))}{degree_sign}")
