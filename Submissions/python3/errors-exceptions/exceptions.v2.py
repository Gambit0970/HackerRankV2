T = int(input())
for i in range(T):
    try:
        a,b = [int(x) for x in input().split()]
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
        
