from menu.clasesGraficos.FigurasGeometricas import *
from menu.clasesGraficos.Rombo import *

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
                self.atributoDeObjetoGrafico=Circulo.Circulo()
            elif self.tipoFigura=="Rombo":
                self.atributoDeObjetoGrafico=Rombo()
            elif  self.tipoFigura=="Rectangulo":
                self.atributoDeObjetoGrafico=Rectangulo.Rectangulo()
            elif  self.tipoFigura=="Cuadrado":
                self.atributoDeObjetoGrafico=Cuadrado.Cuadrado()
            else:
                print ("No esta definida la figura")
                self.atributoDeObjetoGrafico=FigurasGeometricas.FigurasGeometricas() 
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
