class Main:
    xMax=None
    yMax=None
    atributoObjetoGrafico=None
    tipoFigura=None
    def Menu(self):
        print ("Menu")
        print ("1. Elegir el tamano de grafica")
        print ("2. Elegir figura de grafica")
        print ("3. Indicaciones de los atributos")
        print("4. Imprimir dibujo")
        opcion=int(input("Ingresa numero de Menu: "))
        if opcion==1:
            print ("Elegir el tamano de la grafica")
            self.xMax=int(input("Dame le valor maximo de x: "))
            self.yMax=int(input("Dame el valor maximo de y: "))
        if opcion==2:
            print ("Elegir figura de la grafica")
            print (" Circulo \n Rombo \n Rectangulo \n Elipse \n Cuadrado")
            self.tipoFigura=input("Dame un tipo de figura: ")
            print ("Escogiste "+self.tipoFigura)
            if self.tipoFigura=="Circulo":
                self.atributoDeObjetoGrafico=Circulo()
            elif self.tipoFigura=="Rombo":
                self.atributoDeObjetoGrafico=Rombo()
            elif self.tipoFigura=="Rectangulo":
                self.atributoDeObjetoGrafico=Rectangulo()
            elif self.tipoFigura=="Elipse":
                self.atributoDeObjetoGrafico=Elipse()
            elif self.tipoFigura=="Cuadrado":
                self.atributoDeObjetoGrafico=Cuadrado()
            else:
                print ("No esta definida la figura")
                self.atributoDeObjetoGrafico=FigurasGeometricas()
        if opcion==3:
            if self.atributoDeObjetoGrafico !=None:
                self.atributoDeObjetoGrafico.parametros()
            else:
                print ("No hay un objeto definido")
        if opcion==4:
            if self.atributoDeObjetoGrafico !=None:
                if self.atributoDeObjetoGrafico.validar(self.xMax,self.yMax):
                    self.atributoDeObjetoGrafico.graficar()
            else:
                print ("No esta definido el objeto")

class FiguraGrafica(object):
    def graficar():
        print ("Tienes que implementar el metodo graficar")

class ValidarParametros(object):
    def parametros(self):
        print ("Tienes que implementar el metodo parametros")
    def validar(self,x,y):
        print ("tienes que implementar el metodo validar")

class FigurasGeometricas(FiguraGrafica,ValidarParametros):
    Matriz=[]
    __caracter__=None
    __tipo__=None
    def __init__(self,tipo="Sin tipo"):
        self.__tipo__=tipo
    def calcularFigura(self):
        print ("Tienes que sobreescribir este metodo")
        return True

class Rombo(FigurasGeometricas):
    __dM__=None
    __dm__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rombo")
    def parametros(self):
        self.__dM__=int(input("Ingresa un valor para la diagonal mayor: "))
        self.__dm__ = int(input("Ingresa un valor para la diagonal menor: "))
        FigurasGeometricas.__caracter__ = input("Ingresa un caracter: ")
    def calcularFigura(self,y):
        pass
    def graficar(self):
        for x in range(int(self.__dM__)):
            if x <= (self.__dM__)/2:
                print ((int(self.__dm__)-x)*" "+2*x*FigurasGeometricas.__caracter__)
            elif x >= self.__dm__/2:
                print (x*" "+2*(int(self.__dm__)-x)*FigurasGeometricas.__caracter__)
    def validar(self,xMaxima,yMaxima):
        if self.__dM__ <= yMaxima and self.__dm__ <= xMaxima and self.__dm__ >0 and self.__dM__ >= 0:
            return True
        else:
            print ("Debes cambiar los parametros de la figura")
            return False

class Cuadrado(FigurasGeometricas):
    __lado__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,"Cuadrado")
    def parametros(self):
        self.__lado__=int(input("Ingresa el valor del lado: "))
        FigurasGeometricas.__caracter__=str(input("Ingresa un caracter: "))
    def calcularFigura(self):
        for i in range(self.__lado__):
                if i==0 or i==(self.__lado__-1) :
                    print (2*FigurasGeometricas.__caracter__*self.__lado__)
                else:
                    print (FigurasGeometricas.__caracter__ + 2*" "*(self.__lado__-1) + FigurasGeometricas.__caracter__)
    def graficar(self):
        self.calcularFigura()
    def validar(self,xMaximaDeFigura,yMaximaDeFigura):
        if (self.__lado__ <= xMaximaDeFigura and self.__lado__ <= yMaximaDeFigura and self.__lado__>0):
            return True
        else:
            print ("Debes cambiar los parametros de la figura")
            return False

class Circulo(FigurasGeometricas):
    __radio__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,"Circulo")
    def parametros(self):
        self.__radio__=int(input("Ingresa el valor del radio: "))
        FigurasGeometricas.__caracter__ = str(input("Ingresa un caracter: "))
    def calcularFigura(self, x):
        y = round((self.__radio__ ** 2 - x ** 2) ** 0.5)
        return y
    def graficar(self):
        p = ""
        for x in range(-self.__radio__, +self.__radio__, +1):
            for y in range(self.__radio__, -self.__radio__, -1):
                if x < 0:
                    if self.calcularFigura(x) ** 2 == y ** 2:
                        p = p + " " + FigurasGeometricas.__caracter__
                    else:
                        p = p + "  "
                else:
                    if self.calcularFigura(x) ** 2 == y ** 2:
                        p = p + " " + FigurasGeometricas.__caracter__
                    else:
                        p = p + "  "
            print (p)
            p = ""
    def validar(self,xMaxima,yMaxima):
        if (2*self.__radio__ <= xMaxima and 2*self.__radio__ <= yMaxima and self.__radio__ > 0):
            return True
        else:
            print ("Debes cambiar los parametros de la figura")
            return False

class Rectangulo(FigurasGeometricas):
    __base__=None
    __altura__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rectangulo")
    def parametros(self):
        self.__base__=int(input("Ingresa el valor de la base: "))
        self.__altura__=int(input("Ingresa el valor de la altura: "))
        FigurasGeometricas.__caracter__ = str(input("Ingresa un caracter: "))
    def calcularFigura(self):
        for j in range(self.__altura__):
            if j == 0 or j ==(self.__altura__-1):
                print (FigurasGeometricas.__caracter__*self.__base__)
            else:
                print (FigurasGeometricas.__caracter__ + (self.__base__-2)*" " + FigurasGeometricas.__caracter__)
    def graficar(self):
        self.calcularFigura()
    def validar(self,xMaxima,yMaxima):
        if (self.__base__ <= xMaxima and self.__altura__ <= yMaxima and self.__base__ > 0 and self.__altura__ > 0):
            return True
        else:
            print ("Debes cambiar los parametros de la figura")
            return False

class Elipse(FigurasGeometricas):
    __a__=None
    __b__=None
    def __init__(self):
        FigurasGeometricas.__init__(self,"Elipse")
    def calcularFigura(self,x):
        yCuadrada=round((self.__b__**2)*(1-(x**2)/(self.__a__**2)))
        return yCuadrada
    def parametros(self):
        self.__a__=int(input("Ingresa el valor de a: "))
        self.__b__=int(input("Ingresa el valor de b: "))
        FigurasGeometricas.__caracter__ = input("Ingresa un caracter: ")
    def graficar(self):
        p=""
        for x in range(-self.__b__,self.__b__,+1):
            for y in range(self.__a__,-self.__a__,-1):
                if x < 0:
                    if self.calcularFigura(x) == y ** 2:
                        p = p + " " + FigurasGeometricas.__caracter__
                    else:
                        p = p + "  "
                else:
                    if self.calcularFigura(x) == y ** 2:
                        p = p + " " + FigurasGeometricas.__caracter__
                    else:
                        p = p + "  "
            print (p)
            p = ""
    def validar(self,xMax,yMax):
        if 2*self.__a__ <= yMax and 2*self.__b__<= xMax and self.__a__> 0 and self.__b__ >0:
            return True
        else:
            print ("Debes cambiar los parametros de la figura")
            return False