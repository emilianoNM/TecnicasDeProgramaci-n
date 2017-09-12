class Main:
    atributoDeObjetoGrafico=None
    xMax=None
    yMax=None
    tipoFigura=None
    def menu(self):
         print ("menu")
         print("1. Elegir el tamaño de espacio grafico")
         print("2. Elegir figura de  grafica")
         print("3. Indicaciones de los atributos")
         print("4. imprimir dibujo")
         
         menu=input("ingresa nunero de menu")
         if menu=="1":
             print("Elegir tamaño de grafica")
             xMax=int(input("Dame el valor maximo de x"))
             yMax=int(input("Dame el valor maximo de y"))
             print (xMax," ",yMax)
         if menu=="2":
             print("Elegir figura de la grafica")
             print("Circulo")
             print("Rombo")
             print("Rectangulo")
             print("Cuadrado")
             self.tipoFigura=input("Dame el tipo de figura")
             print("Escogiste"+self.tipoFigura)
             if self.tipoFigura=="Ciculo":
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
         if menu=="3":
             if  self.atributoDeObjetoGrafico !=None:
                 
                 self.atributoDeObjetoGrafico.parametros()
             else:
                 ("No hay objeto definido")
         if menu=="4":
             if  self.atributoDeObjetoGrafico !=None:
                  if (self.atributoDeObjetoGrafico.graficar()):
                     self.atributoDeObjetoGrafico.graficar()
class FiguraGrafica(object):
    def Graficar(self):
        print("tienes que implementar el metodo graficar")
class ValidarParametros(object):
    def validar(self):
        print("tienes que implementar el metodo validar")
        print("si no implementas nunca grafica")
        return False
class FigurasGeometricas(FiguraGrafica,ValidarParametros):
      xMaximadefigura=None
      yMaximadefigura=None
      Matriz=[]
      __tipo__=None
      def __init__(self,tipo="sin tipo"):
          self.__tipo__=tipo
          print(self.__tipo__)
      def calcularfigura(self):
          print("tienes que sobrescribir este metodo")
      def parametros(self):
          print("tienes que sobrescribir el metodo"+self.__tipo__)
class Rombo(FigurasGeometricas):
    __x__=None
    __x__=int(input("ingresa el tamaño de la longitud"))
    def __init__(self):
        FigurasGeometricas.__init__(self,"Rombo")
    def graficar(self):
        for i in range (__x__):
	if i<6:
		c=("-"*(5-i))+("c"*i*2)+("-"*(5-i))
		print (c)
	else:
		c=("-"*(i-5))+("c"*(10-i)*2)+("-"*(i-5))
		print (c)
		
    def validar(self):
        print("implementando validar")
        if (self.__x__>0):
            return True
        else:
            print("El valor del parametro es menor a cero")
            return False
    def calcularfigura(self):
        print("calculando los puntos de la figura **")
class Cuadrado(FigurasGeometricas):
      __xmed__=None
      __ymed__=None
      __xmed__=int(input("ingresa el valor de un lado"))
      __ymed__=int(input("ingresa el valor de otro de los lados"))
      def __init__(self):
          FigurasGeometricas.__init__(self,"Cudrado")
      def graficar(self):
          print("******")
      def validar(self):
          print("implementanto validar")
          if (__xmed__==__ymwed__):
              return True
          else:
              print("Lss valores no son iguales")
              return False
      def calcularfigura(self):
          print("calculando los puntos de la figura")
            
class Rectangulo(FigurasGeometricas):
      __base__=None
      __Altura__=None
      __base__=int(input("ingresa el valor de la base"))
      __Altura__=int(input("ingresa el valor de la altura"))
      def __init__(self):
          FigurasGeometricas.__init__(self,"Retangulo")
      def graficar(self):
          print("******")
      def validar(self):
          print("implementando validar")
          if (__base__==__Altura__):
              print("Tus medidas son iguales")
              return False
          else:
              return True
      def calcularfigura(self):
          print("calculando los puntos de la figura")
class Circulo(FigurasGeometricas):
      __radio__=None
      __radio__=int(input("ingresa el valor del radio"))
      def __init__(self):
          FigurasGeometricas.__init__(self,"Circulo")
      def graficar(self):
          print("******")
      def validar(self):
          print("Implementano Validar")
          if(__radio__>0):
              return True
          else:
                print("el radio debe ser mayor a cero")
                return False
      def calcularfigura(self):
          print("Calculando  los puntos de la figura")
class Elipse(FigurasGeometricas):
      __medx__=None
      __medy__=None
      __medx__=int(input("ingresa el valor del diametro mayor"))
      __medy__=int(input("ingresa el valor de la diagonal menor"))
      def __init__(self):
          FigurasGeometricas.__init__(self,"Elipse")
      def graficar(self):
          print("******")
      def validar(self):
          print("implementando validar")
          if (__medx__==__medy__):
              return True
          else:
              print("tus dos medidas no deben ser iguales")
              return False
      def calcularfigura(self):
          print("Calculando los puntos de la figura")
    
    
     


    

                
        
