

def get_earliest_of_two(a,b):
    (ma,da,ya) = a.split('/')
    (mb,db,yb) = b.split('/')
    ca = ya+ma+da 
    cb = yb+mb+db 
    return b if (yb,mb,db) < (ya,ma,da) else a

def date_key(a):
    (m,d,y) = a.split('/')
    return (y,m,d)
    
# multiple argument function
def get_earliest_recursive(a,*b):
    if len(b) == 1:
        return get_earliest_of_two(a,b[0])
    else :
        return get_earliest_of_two(a,get_earliest_recursive(b[0],*b[1:]))

def get_earliest(*b):
    return min(b, key=date_key)

