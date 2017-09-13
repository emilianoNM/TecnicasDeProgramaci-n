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
        print("tienes que implementar el metodo validar")
        
class ValidarParametros(object):
    def validar(self):
        print("tienes que implementar el metodo validar")
        return False
        
class FigurasGeometricas(FiguraGrafica, ValidarParametros):
    xMaximaDeFigura=None
    yMaximaDeFigura=None
    Matriz=[]
    __tipo__=None
    def __init__(self,tipo="Sin tipo"):
        self.__tipo__=tipo
        print(self.__tipo__)
    def calcularFigura(self):
        print("Tienes que seobreescribir este metodo")
    def parametros(self):
        print("Implementa el metodo para obtener los parametros", self.__tipo__)

class Rombo(FigurasGeometricas):
    __x__=None
    def __init__(self):
        FigurasGeometricas.__init__=(self,"Rombo")
    def graficar(self):
        for b in range (self.__x__):
                    if b<(self.__x__-1):
                        c=("-"*(5-b))+("x"*b*2)+("-"*(5-b))
                        print(c)

                    else:
                        for b in range (self.__x__,0,-1):
                            c=("-"*(5-b))+("x"*b*2)+("-"*(5-b))
                            print(c)

class Cuadrado (FigurasGeometricas):
    __x__=None
    def __init__(self):
        FigurasGeometricas.__init__=(self,"Cuadrado")
    def graficar(self):
        for b in range(self.__x__):
            c=self.__x__*"*"
            print(c)
                
    def validar (self):
        self.__x__=input("Dame un numero")
        self.__x__=int(self.__x__)
        print("Implementando validar...")
        if (self.__x__>0):
              return True
        else:
              print("El valor del parametro x es menor que 0")
              return False


