
# coding: utf-8

# In[ ]:

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
                if (self.atributoDeObjetoGrafico.validar()==True):
                         self.atributoDeObjetoGrafico.graficar()
                         
            else :
                 print ("No hay un objeto definido")
class FiguraGrafica():
    def graficar(self):
        print("tienes que iplementar el metodo graficar")
class ValidarParametros():
    def validar(self):
        print("Tienes que implementar el metodo validar")        
class FigurasGeometricas(FiguraGrafica,ValidarParametros):
    xMaximaDeFigura=None
    yMaximaDeFigura=None
    Matriz=[]
    __tipo__=None
    def __init__(self,tipo="sin tipo"):
        self.__tipo__=tipo
        print (self.__tipo__)
    def parametros(self):
        print("implementando parametros para la figura"+self.__tipo__)
    def calcularFigura(self):
        print("tienes que sobreescribir este metodo")
class Rombo(FigurasGeometricas):
    D=int(0)
    d=int(0)
    O=None
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rombo")
    def parametros(self):
        self.D=int(input("ingresa la diagonal mayor "))
        self.d=int(input("ingresa la diagonal menor "))
        self.O=input("ingresa la orientacion del rombo")
        
    def graficar(self):
        empty=" "; char="*";
        if(self.O=="vertical"):
            for i in range(0,self.D+1):
                if i<=self.D/2:
                    print(empty*(self.d-i)+(2*i-1)*char)
                else:
                    print((i-1)*empty+2*char*(self.d-i)+char)
        elif(self.O=="horizontal"):
            for i in range(0,self.d+1):
                if i<=self.d/2:
                    print(empty*(self.D-i)+(2*i-1)*char)
                else:
                    print((i-1)*empty+2*char*(self.D-i)+char)
        else:
             return False
    def validar(self):
        print("implementando validar")
        if (self.D>self.d):
            return True
class Circulo (FigurasGeometricas):
    def __init__(self):
        FigurasGeometricas.__init__(self,"Circulo")
    def graficar(self):
        print("*********")
    def validar(self):
        print("implementando validar")
        return True
    "def parametros(self):"
        
class Cuadrado(FigurasGeometricas):
    def __init__(self):
        FigurasGeometricas.__init__(self,"Cuadrado")
    def graficar(self):
        print("esto es un cuadrado [] ")
    def validar(self):
        print("implementando validar")
        return True
    "def parametros(self):"

class Rectangulo(FigurasGeometricas):
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rectangulo")
    def graficar(self):
        print("esto es un Rectangulo [__] ")
    def validar(self):
        print("implementando validar")
        return True
    "def parametros(self):"

