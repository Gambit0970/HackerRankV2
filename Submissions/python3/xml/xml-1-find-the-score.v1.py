

def get_attr_number(node):
    x=len(node.attrib.keys())
    if len(node)>=2:
        for ch in node:
            x+=get_attr_number(ch)
    return(x)

