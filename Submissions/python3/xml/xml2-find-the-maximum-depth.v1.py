

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level+=1
    for ch in elem:
        depth(ch, level)
    if level>maxdepth:
        maxdepth=level
    # your code goes here

