from menu.clasesGraficos.interfaces.FiguraGrafica import *
from menu.clasesGraficos.interfaces.ValidarParametros import *
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
