
def sun_angle(time):
    a = (int(time.split(":")[0])-6)*60
    b = (int(time.split(":")[1]))
    kat = (a + b) * 0.25
    # 0.25 na kazda minute
    if kat < 0 or kat > 180:        # zawezenie zakresu
        return "I don't see the sun!"
    return kat


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")