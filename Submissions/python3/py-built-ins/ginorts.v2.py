S = [x for x in input()]
Sl = sorted([x for x in S if x.islower()])
Su = sorted([x for x in S if x.isupper()])
So = [str(_) for _ in sorted([int(x) for x in S if x.isdigit() and int(x)%2==1])]
Se = [str(_) for _ in sorted([int(x) for x in S if x.isdigit() and int(x)%2==0])]
print(''.join(Sl + Su + So + Se))

