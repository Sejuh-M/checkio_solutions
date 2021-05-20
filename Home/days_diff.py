from datetime import date
def days_diff(a, b):

    f = date(a[0], a[1], a[2]) # wyczytane z dokumentacji datetime
    l = date(b[0], b[1], b[2])
    c = abs(f - l)

    return c.days


if __name__ == '__main__':
    print("Example:")
    print(days_diff((2014, 1, 1), (2014, 8, 27)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")