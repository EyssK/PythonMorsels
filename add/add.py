

def add(a,b):
    
    # works only dor depth 1 lists
    # return [ x+y for (x,y) in zip(a,b) ]

    l = list()
    for (x,y) in zip(a,b):
        if type(x) == type(tuple()) or type(x) == type(list()):
            l.append( add(x,y))
        else:
            l.append(x+y)
    return(l)
