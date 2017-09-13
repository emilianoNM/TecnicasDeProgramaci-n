class Rombo(FigurasGeometricas):
    __x__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rombo")
    def graficar(self):
        print ("*************")
    def validar(self):
        print ("Implementando validar")
        if (self.__x__>0):
            return True
        else:
            print ("El valor del parametro x es menor que cero")
            return False
    def calcularFigura(self):
        print ("calculando puntos de la figura")
