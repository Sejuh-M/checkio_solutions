#!/usr/bin/env checkio --domain=py run all-upper

# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.
# 
# Input:A string.
# 
# Output:a boolean.
# 
# Precondition:a-z, A-Z, 1-9 and spaces
# 
# 
# END_DESC

def is_all_upper(text: str) -> bool:
    if text.isupper() == True: #sprawdzennie czy text jest upper, isupper - zwraca wartosc logiczna
        a = True
    elif text == "": #warunek dla linii 19
        a = True
    elif text.isspace() == True:
        a = True
    elif text.isnumeric() == True:
        a = True
    else:
        a = False
    return a


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")