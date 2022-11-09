import math
def obwod(P1,P2,P3):
    def odlegloscp1p2(P1,P2):
        x = ((P2[0]-P1[0])**2)+((P2[1]-P1[1])**2)
        dlugoscx = x
        return  dlugoscx
    def odlegloscp1p3(P1,P3):
        y = ((P3[0]-P1[0])**2)+((P3[1]-P1[1])**2)
        dlugoscy = y
        return dlugoscy
    def odlegloscp2p3(P2,P3):
        z = ((P3[0]-P2[0])**2)+((P3[1]-P2[1])**2)
        dlugoscz = z
        return dlugoscz
    return obw


obwod([0,0],[0,4],[3,0])