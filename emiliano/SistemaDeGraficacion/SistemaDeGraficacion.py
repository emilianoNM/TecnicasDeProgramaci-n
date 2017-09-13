

class FiguraGrafica(object):
    def graficar(self):
        print ("Tienes que implementar el mentodo graficar")
class ValidarParametros(object):
    def validar(self):
        print ("Tienes que implementar el mentodo validar")
        print ("Si no implementas nunca va graficar")
        return False

class FigurasGeometricas(FiguraGrafica,ValidarParametros):
      xMaximaDeFigura=None
      yMaximaDeFigura=None
      Matriz=[]
      __tipo__=None
      def __init__(self,tipo="Sin Tipo"):
            self.__tipo__=tipo
            print (self.__tipo__)
      def calcularFigura(self):
          print ("tienes que sobreescribir este metodo")
      def parametros(self):
          print ("Implemeta el metodo para obtener los parametros "+self.__tipo__)

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
