cube = lambda x:x**3 # complete the lambda function 

def fib(n):
    if n == 0:
        x=0
    elif n == 1:
        x=1
    else:
        x=fib(n-1)+fib(n-2)
    #print('fib',n,x)
    return x

def fibonacci(n):
    x=list()
    for i in range(n):
        x.append (fib(i))
    
    #print(x)
    return x
    # return a list of fibonacci numbers

