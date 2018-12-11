
def getOnlyLetters(s):
    if s[0].isalpha() == False :
        return getOnlyLetters(s[1:])
    elif s[-1].isalpha() == False :
        return getOnlyLetters(s[:-1])
    else: 
        return s

def count_words(s):
    D = dict()
    L = s.split(' ')
    for _w in L:
        w = _w.lower()
        w = getOnlyLetters(w)
        if w in D:
            D[w] = D[w] + 1
        else:
            D[w]=1
    
    return D

