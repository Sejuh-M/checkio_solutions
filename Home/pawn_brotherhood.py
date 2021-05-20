#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# 
# END_DESC

def safe_pawns(pawns: set) -> int:
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    pawns = list({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
    # i = 0
    # a = ""
    # b = ""
    # pozycje = []
    # for words in pawns:
    #     for letter in pawns[i]:
    #          if letter.isalpha():
    #             skos1 = ((chr(ord(letter)-1)))
    #             skos2 = ((chr(ord(letter)+1)))
    #             a = a + (skos1)
    #             b = b + (skos2)
    #             print(skos1)
    #             print(skos2)
    #
    #          else:
    #             skosl = ((chr(ord(letter) - 1)))
    #             a = a + (skosl)
    #             b = b + (skosl)
    #             print(skosl)
    #
    #     i += 1
    #
    # print(a)
    # pozycje=[]
    # licznik = 0
    # for z in a:
    #     if licznik < len(a):
    #         print(a[licznik:licznik+2])
    #         pozycje.append(a[licznik:licznik+2])
    #         licznik += 2
    # pozycjeb = []
    # licznik = 0
    # for z in b:
    #     if licznik < len(b):
    #         print(b[licznik:licznik+2])
    #         pozycjeb.append(b[licznik:licznik+2])
    #         licznik += 2
    # print(b)
    # print(pozycje)
    # print(pozycjeb)
    # mozliwości = pozycje + pozycjeb
    # bez_powtorek = list(set(mozliwości))
    # wynik = len(set(mozliwości)&set(pawns))
    #
    # print(mozliwości)
    # print(bez_powtorek)
    # counter = 0
    #
    # print(wynik)