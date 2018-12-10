def add(a,*b):
    #print("add"+str(a)+str(b))
    return(add2(a,*b))
#    else :
#        return(add2(a,add_multiple(b[0],*b[1:])))

def add2(a,b):
    
    # works only dor depth 1 lists
    # return [ x+y for (x,y) in zip(a,b) ]

    #print("add2"+str(a)+str(b))

    l = list()
    for (x,y) in zip(a,b):
        if type(x) == type(tuple()) or type(x) == type(list()):
            l.append( add2(x,y))
        else:
            l.append(x+y)
    return(l)
