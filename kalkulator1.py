while 1:

    print("Obliczę za ciebie wszystko (w granicach możliwości)")

    x = int(input("podaj pierwszą liczbę"))
    y = int(input("podaj drugą liczbę"))

    z = int(input("Co chcesz zrobić? 1: Dodawanie, 2: Odejmowanie, 3: Mnożenie, 4: Dzielenie, 5: Dzielenie całkowite, 6: Wynik z reszty dzielenia, 7: Potęgowanie"))

    wynik = 0

    if z == 1:
        wynik = x + y

    if z == 2:
        wynik = x - y

    if z == 3:
        wynik = x * y

    if z == 4:
        wynik = x / y

    if z == 5:
        wynik = x // y

    if z == 6:
        wynik = x % y

    if z == 7:
        wynik = x ** y

    print("Wynik:", wynik)
    print("Możesz ponowić operację:")

    continue