class Escuela():
    nombre=[]
    sexo=[]
    edad=[]
    estatura=[]
    peso=[]
    numero=None
    def menu(self):
        print """        1. Escribir el archivo de datos
        2. Leer y procesar los datos
        3. Terminar"""
        opcion=input("Ingresa una opcion: ")
        x=opciones()
        if opcion == 1:
            x.opcion1()
        elif opcion == 2:
            x.opcion2()
        elif opcion == 3:
            x.opcion3()

class opciones(Escuela):
    def opcion1(self):
        documento = open("/Users/AlejnadroZapett/Desktop/alumnos.txt", "w")
        documento.write("Datos de los alumnos \n")
        Escuela.numero=input("Cuantos alumnos son? ")
        for i in range(Escuela.numero):
            print("Ingresa los datos del alumno "+str(i+1))
            Escuela.nombre.append(input("Nombre: "))
            Escuela.sexo.append(input("Sexo: "))
            Escuela.edad.append(input("Edad: "))
            Escuela.estatura.append(input("Estatura: "))
            Escuela.peso.append(input("Peso: "))
            documento.write("\nAlumno no."+str(i+1)+"\n Nombre: "+Escuela.nombre[i]+"\n Sexo: "+Escuela.sexo[i])
            documento.write("\n Edad: "+str(Escuela.edad[i]))
            documento.write("\n Estatura: "+str(Escuela.estatura[i])+"\n Peso: "+str(Escuela.peso[i]))
        documento.close()
    def opcion2(self):
        if Escuela.numero != None:
            print ("\n Los datos son: ")
            documento = open("/Users/AlejnadroZapett/Desktop/alumnos.txt", "r")
            print documento.read()
            documento.close()
            suma=0
            promedio=0
            for i in range(Escuela.numero):
                if Escuela.sexo[i] == "masculino" or Escuela.sexo[i] == "Masculino":
                    suma=suma+Escuela.edad[i]
                promedio=suma/Escuela.numero
                if Escuela.estatura[i] >= 1.65:
                    print (Escuela.nombre[i]+" tiene una estatura de "+str(Escuela.estatura[i]))
            print ("El promedio de edad de los hombres es: "+str(promedio))
        else:
            print ("No has ingresado datos de los alumnos")
    def opcion3(self):
        print ("Se termino de ingresar y procesar los datos de los alumnos")