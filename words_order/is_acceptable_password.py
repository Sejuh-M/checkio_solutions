# Taken from mission Acceptable Password V

# Taken from mission Acceptable Password IV

# Taken from mission Acceptable Password III

# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        x = True
    else:
        x = False
    return x


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        for letter in password:
            if letter.isdigit() == 1:
                result = True
            else:
                result = False
    else:
        result = False
    return result


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    answer = ''
    if len(password) > 6:
        for letter in password:
            if letter.isnumeric() == 1:
                result = True
                for l in password:
                    if l.isalpha() == 1:
                        return True
                    else:
                        answer = False
            else:
                answer = False

    else:
        answer = False

    return answer


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    answer = ''
    if len(password) > 6:
        for letter in password:
            if letter.isnumeric() == 1:
                result = True
                for l in password:
                    if l.isalpha() == 1:
                        return True
                    else:
                        if len(password) > 9:
                            return True
                        else:
                            answer = False
            else:
                if len(password) > 9:
                    return True
                else:
                    answer = False

    else:
        answer = False

    return answer


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(a):
    answer = ''
    a = a.lower()
    if "password" in a:
        return False
    else:
        password = a
        if len(password) > 6:
            for letter in password:
                if letter.isnumeric() == 1:
                    result = True
                    for l in password:
                        if l.isalpha() == 1:
                            return True
                        else:
                            if len(password) > 9:
                                return True
                            else:
                                answer = False
                else:
                    if len(password) > 9:
                        return True
                    else:
                        answer = False

        else:
            answer = False

    return answer


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

def is_acceptable_password(a):
    answer = ''
    if len(set(a)) > 2:
        a = a.lower()
        if "password" in a:
            return False
        else:
            password = a
            if len(password) > 6:
                for letter in password:
                    if letter.isnumeric() == 1:
                        result = True
                        for l in password:
                            if l.isalpha() == 1:
                                return True
                            else:
                                if len(password) > 9:
                                    return True
                                else:
                                    answer = False
                    else:
                        if len(password) > 9:
                            return True
                        else:
                            answer = False

            else:
                answer = False
    else:
        return False

    return answer


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
