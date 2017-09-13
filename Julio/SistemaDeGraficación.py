class Main():
    AtributoDeObjetoGrafico=None
    xMax=None
    yMax=None
    def menu(self):
        print("Menu")
        print("1.-Elegir el tamaño del espacio de la grafica")
        print("2.-Elegir la figura de grafica")
        print("3.-Indicaciones de los atributos")
        print("4.-Imprimir dibujo")

        menu=input("Ingresa número de Menú: ")
        if menu=="1":
            print ("Elegir tamaño de Gráfica")
            xMax=int(input("Dame el valor máximo de x"))
            yMax=int(input("Dame el valor máximo de y"))
            print (xMax,",",yMax)
            pass
        if menu=="2":
            print("Elegir figura a graficar")
            print("Circulo")
            print("Rombo")
            print("Rectangulo")
            print("Cuadrado")
            self.tipoFigura=input("Dame el tipo de figura")
            print("Escogiste "+self.tipoFigura)
            if self.tipoFigura=="Circulo":
                self.AtributoDeObjetoGrafico=Circulo()
            elif self.tipoFigura=="Rombo":
                self.AtributoDeObjetoGrafico=Rombo()
            elif self.tipoFigura=="Rectangulo":
                self.AtributoDeObjetoGrafico=Rectangulo()
            elif self.tipoFigura=="Cuadrado":
                self.AtributoDeObjetoGrafico=Cuadrado()
            else:
                print("No esta definida la figura")
                self.AtributoDeObjetoGrafico=FigurasGeometricas()
        if menu=="3":
            if self.AtributoDeObjetoGrafico !=None:
                self.AtributoDeObjetoGrafico.parametros()
            else:
                print("No hay un objeto definido")
        if menu=="4":
            if self.AtributoDeObjetoGrafico !=None:
                if (self.AtributoDeObjetoGrafico.validar()):
                    self.AtributoDeObjetoGrafico.graficar()
                else:
                    print("No hay un objeto definido")
class FiguraGrafica(object):
    def graficar(self):
        print("Tienes que implementar el método graficar")
class ValidarParametros(object):
    def validar(self):
        print("Tienes que implementar el método validar")
        print("Si no implementas nunca va a graficar")
        return False
class FigurasGeometricas(FiguraGrafica,ValidarParametros):
    xMaximaDeFigura=None
    yMaximaDeFigura=None
    Matriz=[]
    __tipo__=None
    def __init__(self,tipo="Sin Tipo"):
        self.__tipo__=tipo
        print(self.__tipo__)
    def calcularFigura(self):
        print ("Tienes que sobreescribir este método")
    def parametros(self):
        print("Implementa el metodo para obtener los parametros "+self.__tipo__)
                

class Rombo(FigurasGeometricas):
    __linea__=None:
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rombo")
    def graficar(self):
        print("***********")
    def validar(self):
        print("Implementando validar")
        if(self__x__>0):
            return True
        else:
            print("El valor del parametro linea es menor que cero")
            return False
    def calcularFigura(self):
        print("calculando puntos de la figura")

class Circulo(FigurasGeometricas):
    __radio__=None:
    def __init__(self):
        FigurasGeometricas.__init__(self,"Círculo")
    def graficar(self):
        print("***********")
    def validar(self):
        print("Implementando validar")
        if (self__x__>0):
            return True
        else:
            print("El valor del parametro radio es menor que cero")
            return False
    def calcularFigura(self):
        print("calculando puntos de la figura")

class Rectangulo(FigurasGeometricas):
    __base__=None:
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rectangulo")
    def graficar(self):
        print("***********")
    def validar(self):
        print("Implementando validar")
        if (self__x__>0):
            return True
        else:
            print("El valor del parametro base es menor que cero")
            return False
    def calcularFigura(self):
        print("calculando puntos de la figura")

class Cuadrado(FigurasGeometricas):
    __lado__=None:
    def __init__(self):
        FigurasGeometricas.__init__(self,"Cuadrado")
    def graficar(self):
        print("***********")
    def validar(self):
        print("Implementando validar")
        if(self__x__>0):
            return True
        else:
            print("El valor del parametro lado es menor que cero")
            return False
    def calcularFigura(self)_
        print("calculando puntos de la figura")
    
        
