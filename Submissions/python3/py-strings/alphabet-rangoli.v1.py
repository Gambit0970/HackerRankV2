def print_rangoli(size):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    chrs = abc[:size][::-1]
    for i in range(size*2-1):
        if i < size:
            fwd = chrs[:i+1]
        else:
            fwd = chrs[:size*2-i-1]
        #print(fwd)
        bck = fwd[:-1]
        print("-".join(fwd+bck[::-1]).center(size*4-3,"-"))
    # your code goes here

