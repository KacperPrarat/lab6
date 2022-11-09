import math
def obwod(P1,P2,P3):
    def odlegloscp1p2(P1,P2):
        x = ((P2[0]-P1[0])**2)+((P2[1]-P1[1])**2)
        dlugoscx = x
        return  math.sqrt(dlugoscx)
    def odlegloscp1p3(P1,P3):
        y = ((P3[0]-P1[0])**2)+((P3[1]-P1[1])**2)
        dlugoscy = y
        return math.sqrt(dlugoscy)
    def odlegloscp2p3(P2,P3):
        z = ((P3[0]-P2[0])**2)+((P3[1]-P2[1])**2)
        dlugoscz = z
        return math.sqrt(dlugoscz)
    return (odlegloscp1p2(P1,P2) + odlegloscp1p3(P1,P3) + odlegloscp2p3(P2,P3))


print(obwod([7.5,-8],[-2,0],[7,12]))
