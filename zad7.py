def szukajWliscie(lista,a):
    wynik = 0
    for i in lista:
        if i == a:
            wynik = wynik +1
    print(wynik)

szukajWliscie([2,4,5,6,7,7,7,8,9,2],2)