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
