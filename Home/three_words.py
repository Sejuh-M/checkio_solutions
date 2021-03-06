
def checkio(words: str) -> bool:
    licznik = 0
    pamietnik = 0
    for w in words.split():
        if w.isalpha():
            licznik += 1
            if licznik >= 3:
                pamietnik = licznik
        else:
            licznik = 0
    if pamietnik >= 3:
        result = True
    else:
        result = False
    return result
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")