import math
def obwodTrojkata(P1,P2,P3):
    def odlegloscp1p2(P1, P2):
        x = ((P2[0] - P1[0]) ** 2) + ((P2[1] - P1[1]) ** 2)
        return math.sqrt(x)
