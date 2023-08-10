if __name__ == '__main__':
    n = int(input())
    arr = [int(n) for n in input().split()]
    arr[:] =  (value for value in arr if value != max(arr))
    print(max(arr))
