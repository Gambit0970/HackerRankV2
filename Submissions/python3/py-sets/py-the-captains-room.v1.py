K = int(input())
arr = sorted([int(x) for x in input().split()])
for i in range(0,len(arr),K):
    try:
        if arr[i] != arr[i+K-1]:
            break
    except:
        break
print(arr[i])
