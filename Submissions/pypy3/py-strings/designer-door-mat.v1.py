pattern = '.|.'
lines,length = [int(x) for x in input().split()]
mid = "WELCOME".center(length, '-')
for i in range(lines):
    if i < lines//2:
        rp = 1+2*i
        print(str(pattern*(rp)).center(length,'-'))
    elif i > lines//2:
        rp = (lines-i)*2-1
        print(str(pattern*(rp)).center(length,'-'))
    else:
        print(mid)

