from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    i = 0
    a = 0
    b = ''
    result = ()
    if items == []:
        result = ('', 0)
    else:

        for word in items:
            print(items[i])
            if type(word) is int:
                a = a + int(word)
                print(a)
                print(items[i])
            else:
                b = b + str(word)
                print(b)
            result = (b, a)
        i += 1

    return result


if __name__ == '__main__':
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ('', 0)
    assert sum_by_types([1, 2, 3]) == ('', 6)
    assert sum_by_types(['1', 2, 3]) == ('1', 5)
    assert sum_by_types(['1', '2', 3]) == ('12', 3)
    assert sum_by_types(['1', '2', '3']) == ('123', 0)
    assert sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
