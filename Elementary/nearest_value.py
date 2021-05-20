
def nearest_value(values: set, one: int) -> int:
    if one in values:
        result = one
    else:
        c = list(values)
        jeden = one
        dwa = one
        if one > min(c) and one < max(c):
            while jeden not in values:
                jeden = jeden - 1
            while dwa not in values:
                dwa = dwa + 1
            if one - jeden < dwa - one:
                    result = jeden
            elif one - jeden > dwa - one:
                    result = dwa
            else:
                result = jeden
        elif one < min(c):
            while jeden not in values:
                jeden = jeden + 1
                result = jeden
        elif one > max(c):
            while dwa not in values:
                dwa = dwa - 1
                result = dwa

    return result


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")