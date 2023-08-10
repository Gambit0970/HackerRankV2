def wrapper(f):
    def fun(l):
        for i,e in enumerate(l):
            l[i] = f"+91 {l[i][-10:-5]} {l[i][-5:]}"
        f(l)
        # complete the function
    return fun

