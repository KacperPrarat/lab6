def pietro(a):
    print(10*a)
    print(3*a+4*" "+3*a)
    print(3*a+4*a +3*a)
    print(10*a)
def dach(b):
    print( 2 * b)
    print(4 * b)
    print(6* b)
    print(8* b)
    print(10* b)

def rysujDomek(liczbapieter,b,a):
    dach(b)
    for i in range(liczbapieter):
        pietro(a)

rysujDomek(3,"#","$")