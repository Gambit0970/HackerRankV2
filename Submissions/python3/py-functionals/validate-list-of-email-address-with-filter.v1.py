import re

def fun(s):
    pattern="^[a-zA-Z][a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    #print(re.match(pattern,s))
    return (True if re.match(pattern,s)!=None else False)
    
    # return True if s is a valid email, else return False

