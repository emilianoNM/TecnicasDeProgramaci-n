class Main():
    atributoDeObjetoGrafico=None
    xMax=None
    yMax=None
    tipoFigura=None
    def menu(self):
        print ("Menu")
        print("Menu: ")
        print("1.- Elegir el tamaño del espacio de grafica")
        print("2.- Elegir figura de grafica")
        print("3.- Indicaciones de los atributos")
        print("4.- Imprimir dibujo")

        opcion=input("Ingresa numero de Menú: ")

        if opcion=="1":
            print ("Elegir tamaño de Grafica")
            xMax=int(input("Dame el valor Maximo de x"))
            yMax=int(input("Dame el valor Maximo de y"))
            print (xMax," , ",yMax)
        if opcion=="2":
            print ("Elegir figura a grafica")
            print  ("Circulo")
            print  ("Rombo")
            print  ("Rectangulo")
            print  ("Cuadrado")
            self.tipoFigura=input("Dame el tipo de figura") 
            print ("Escogiste "+self.tipoFigura)
            if self.tipoFigura=="Circulo":
                self.atributoDeObjetoGrafico=Circulo()
            elif self.tipoFigura=="Rombo":
                self.atributoDeObjetoGrafico=Rombo()
            elif self.tipoFigura=="Rectangulo":
                self.atributoDeObjetoGrafico=Rectangulo()
            elif self.tipoFigura=="Cuadrado":
                self.atributoDeObjetoGrafico=Cuadrado()
            else:
                print ("No esta definida la figura")
                self.atributoDeObjetoGrafico=FigurasGeometricas() 
        if opcion=="3":
            if self.atributoDeObjetoGrafico !=None:
                self.atributoDeObjetoGrafico.parametros()
            else :
                print ("No hay un objeto definido")
        if opcion=="4":
            if self.atributoDeObjetoGrafico !=None:
                if (self.atributoDeObjetoGrafico.validar()):
                         self.atributoDeObjetoGrafico.graficar()
                         
            else :
                 print ("No hay un objeto definido")

class FiguraGrafica(object):
    def graficar(self):
        print('Tienes que implementar el metodo graficar')
class ValidarParametros(object):
    def validar(self):
        print('Tienes que implementar el metodo validar')
        return False
class FigurasGeometricas(FiguraGrafica,ValidarParametros):
      xMaximaDeFiguras=None
      yMaximadeFiguras=None
      Matriz=[]
      __tipo__=None
      #atributo
      def __init__(self,tipo='sin tipo'):
          self.__tipo__=tipo
          print (self.__tipo__)
      def calcularFigura(self):
          print ('tienes que sobreescribir este metodo')
          def parametros(self):
              print('implementa el metodo para obtener los parametros')

class Rombo(FigurasGeometricas):
    __x__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,'Rombo')
    def graficar(self):
        print('****************')
    def validar(self):
        print ('Implementando validar')
        
        if  (self.__x__>0):
         return False
        else:
         return True
    def calcularFigura(self):
        print('calcular puntos de la figura ')

class Rectangulo(FigurasGeometricas):
    __x__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,'Rectangulo')
    def graficar(self):
        print('****************')
    def validar(self):
        print ('Implementando validar')
        
        if  (self.__x__>0):
         return False
        else:
         return True
    def calcularFigura(self):
        print('calcular puntos de la figura ')

class Cuadrado(FigurasGeometricas):
    __x__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,'Cuadrado')
    def graficar(self):
        print('****************')
    def validar(self):
        print ('Implementando validar')
        
        if  (self.__x__>0):
         return False
        else:
         return True
    def calcularFigura(self):
        print('calcular puntos de la figura ')

class Circulo(FigurasGeometricas):
    __x__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,'Circulo')
    def graficar(self):
        print('****************')
    def validar(self):
        print ('Implementando validar')
        
        if  (self.__x__>0):
         return False
        else:
         return True
    def calcularFigura(self):
        print('calcular puntos de la figura ')
