

def wrap(string, max_width):
    newstr = "\n".join(string[i:i+max_width] for i in range(0,len(string),max_width))
    #for i in range(0,len(string),max_width):
    #    newstr += string[i:i+max_width] + "\n"
    return newstr

