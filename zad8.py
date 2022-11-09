def szukajWliscie(lista,a):
    wynik = 0
    for i in lista:
        if i == a:
            wynik = wynik +1
    return  wynik
x = szukajWliscie([1,2,3,4,5],5)
print(x)

szukajWliscie([2,4,5,6,7,7,7,8,9,2],2)