def end_zeros(num: int) -> int:
    for i in range(len(str(num))):
        if num % 10 == 0:
            num = num / 10
            x = i
        else:
            x = 0
    return x


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
