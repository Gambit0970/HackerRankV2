aN = int(input())
a = set([int(x) for x in input().split()])
iN = int(input())
for i in range(iN):
    inst, icount = [x for x in input().split()]
    b = set([int(x) for x in input().split()])
    if inst == 'intersection_update':
        a &= b
    elif inst == 'update':
        a |= b
    elif inst == 'symmetric_difference_update':
        a ^= b
    elif inst == 'difference_update':
        a -= b
    else:
        print(f"Unknown instruction: {inst}")
print(sum(a))
