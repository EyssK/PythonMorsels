
def getOnlyLetters(s):
    if s[0].isalpha() == False :
        return getOnlyLetters(s[1:])
    elif s[-1].isalpha() == False :
        return getOnlyLetters(s[:-1])
    else: 
        return s

def count_words(s):
    D = dict()
    for w in s.lower().split():
        w = getOnlyLetters(w)
        if w in D:
            D[w] += 1
        else:
            D[w]=1
    
    return D



# Other solution :
if __name__ == "__main__":
    
    from collections import Counter

    def test(a,b):
        if a==b:
            print("OK")
        else:
            raise ValueError("Test Failed\n"+ str(a) + " != " + str(b))

    def count_words(s):
        return Counter(s.lower().split())


    actual = count_words("oh what a day what a lovely day")
    expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
    test(actual,expected)

    actual = count_words("don't stop believing")
    expected = {"don't": 1, 'stop': 1, 'believing': 1}
    test(actual,expected)

    actual = count_words("Oh what a day what a lovely day")
    expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
    test(actual,expected)
