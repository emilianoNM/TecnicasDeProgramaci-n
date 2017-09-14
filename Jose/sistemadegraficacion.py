class Main():
    atributoDeObjetoGrafico=None
    xMax=None
    yMax=None
    tipoFigura=None
    
    def opcion(self):
        print ("Menu: ")
        print ("1. Elegir dimensiones de espacio de grafica")
        print ("2. Elegir figura de grafica")
        print ("3.indicaciones de los atributos")
        print ("4. Imprimir dibujo")

        opcion=input("Ingresa numero de Menu:  ")


        if opcion=="1":
            print ("Dame el tamaño de Grafica")
            xMax=int(input("Dame el valor Maximo de x: "))            
            yMax=int(input("Dame el valor Maximo de y: "))
            print(xMax," , ",yMax)
        if opcion=="2":
            print ("Elegir figura de grafica")
            print("Circulo")
            print("Rombo")
            print("Rectangulo")
            print("Cuadro")
            self.tipoFigura=input("Dame el tipo de figura: ")
            print("Escogiste"+self.tipoFigura)
            if self.tipoFigura=="Circulo":
                self.atributoDeObjetoGrafico=Circulo()
            elif self.tipoFigura=="Rombo":
                self.atributoDeObjetoGrafico=Rombo()
            elif self.tipoFigura=="Rectangulo":
                self.atributoDeObjetoGrafico=Rectangulo() 
            elif self.tipoFigura=="Cuadrado":
                self.atributoDeObjetoGrafico=Cuadrado()
            else:
                print("No esta definida")
                self.atributoDeObjetoGrafico=FigurasGeometricas()        
        if opcion=="3":
            if self.atributoDeObjetoGrafico !=None:
               self.atributoDeObjetoGrafico.parametros()
            else :
                print ("No hay objeto definido")
        if opcion=="4":
            if self.atributoDeObjetoGrafico !=None:
               if (self.atributoDeObjetoGrafico.validar()):
                         self.atributoDeObjetoGrafico.graficar()
            else :
                print ("No hay objeto definido")

class FiguraGrafica():
    def graficar():
        if "Cuadro":
            print(Circulo)
        elif "Rectangulo":
            print(Rectangulo)
        elif "Circulo":
            print (Circulo)
        elif "Rombo":
            print (Rombo)
        else:
            print("Tienes que implementar el metodo graficar")
class ValidarParametros():
    def validar():
        if "Cuadro":
           if xMax>lado:
               print("Es posible graficar en este eje ")
           if yMax>lado:
               print("Es posible graficar en este eje")
           else:
               print("Imposible graficar")
        elif "Rectangulo":
            if xMax>base:
                print("Es posible graficar en este eje ")
            if yMax>altura:
                print("Es posible graficar en este eje ")
        elif "Circulo":
            if xMax>radio:
              if yMax>radio:
                print ("Es posible graficar")
        
        #print("Tienes que implementar el metodo validar")
        #print("Si no nuca va a graficar")
        #return False
        
class FigurasGeometricas(FiguraGrafica,ValidarParametros):
      xMaximaDeFigura=None
      yMaximaDeFigura=None
      Matriz=[]
      __tipo__=None
      def  __init__(self,tipo="Sin tipo"):
            self.__tipo__=tipo
            print (self.__tipo__)
      def calcularFigura(self):
        print ("tienes que sobrescribir este metodo")
      def parametros(self):
         if "Cuadro":
            lado=input("Dame el tamaño de los lados: ")
         elif "Rectangulo":
            base=input("Dame el tamaño de la base: ")
            altura=input ("Dame el tamaño de la altura: ")
         elif "Circulo":
            radio=input("Dame el tamaño del radio: ")
         elif "Rombo":
            diagmay=input("Dame el valor de la diagonal mayor: ")
            dagmen=input("Dame el valor de la diagonal menor: ")
         else:
            print ("No existe")
          
           # print ("Implementa el metodo para obtener los parametros"+self.__tipo__)

    
class Rombo (FigurasGeometricas):
    __x__=None
    def __init__(self):
         FigurasGeometricas.__init__(self,"Rombo")
    def graficar(self):
        
        def validar(self):
            print("Implementar validar")
        if (self.__x__>0):
            return True
        else:
            print ("El valor del parametro x es menor que cero")
            return False
class Circulo (FigurasGeometricas):
    __x__=None
    def __init__(self):
         FigurasGeometricas.__init__(self,"Circulo")
    def graficar(self):
        print("**********")
    def validar(self):
        print("Implementar validar")
        if (self.__x__>0):
            return True
        else:
            print ("El valor del parametro x es menor que cero")
            return False
class Rectangulo (FigurasGeometricas):
    __x__=None
    def __init__(self):
         FigurasGeometricas.__init__(self,"Rectangulo")
    def graficar(self):
        print("**********")
    def validar(self):
        print("Implementar validar")
        if (self.__x__>0):
            return True
        else:
            print ("El valor del parametro x es menor que cero")
            return False

class Cuadro (FigurasGeometricas):
    __x__=None
    def __init__(self):
         FigurasGeometricas.__init__(self,"Cuadro")
    def graficar(self):
        for i in range (lado,o,-1):
            print ("#")
        for j in range (0,lado,+1):
            print ("#")
    def validar(self):
        print("Implementar validar")
        if (self.__x__>0):
            return True
        else:
            print ("El valor del parametro x es menor que cero")
            return False
