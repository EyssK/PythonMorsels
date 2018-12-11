# -*- coding: utf-8 -*-
def add(a,*b):
    """add any number of matrices of the same dimension 
        with respect to the indexes

    Args:
        a (list): first matrix
        b : variable length of matrices

    Raises:
        ValueError: if input matrices doesn't have the same dimension
    """
    if len(b) == 1:
        return(add2(a,*b))
    else :
        return(add2(a,add(b[0],*b[1:])))



def add2(a,b):
    """add 2 matrices of the same dimension
    
    Args:
        a (list): first matrix
        b (list): second matrix

    Return:
        list: The addition of the 2 matrices

    Raises:
        ValueError: if a and b doesn't have the same dimension

    """
    if len(a) != len(b):
        raise ValueError

    l = list()
    for x,y in zip(a,b):
        if type(x) == type(tuple()) or type(x) == type(list()):
            l.append( add2(x,y))
        else:
            l.append(x+y)
    return(l)



