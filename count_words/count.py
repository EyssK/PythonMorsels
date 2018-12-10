

def count_words(s):
    D = dict()
    L = s.split(' ')
    for _w in L:
        w = _w.lower()
        if w in D:
            D[w] = D[w] + 1
        else:
            D[w]=1
    
    return D



