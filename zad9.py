import math
P1 = [-1,-1]
P2 = [2,3]
def odleglosc(P1,P2):
    x = ((P2[0]-P1[0])**2)+((P2[1]-P1[1])**2)
    return math.sqrt(x)

print(odleglosc([7.5,-8],[-2,0]))