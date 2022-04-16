'''
Programa para solicitar el nombre, apellido, edad y la nota promedio de 5 estudiantes de un curso
de computación.

'''

def SENA():
    #Variables
    SumaNotas=0
    Estudiantes=5
    
    for i in range(Estudiantes):

        # Pedidos datos del estudiante
        print("Estudiante {}".format(i+1))
        Nombre=str.lower(input("Ingrese nombre: "))
        Apellido=str.lower(input("Ingrese apellido: "))
        Edad=int(input("Ingrese su edad: "))

        #Conditional
        while(True):
            try:
                Nota=float(input("Ingrese nota: "))
                if Nota >= 0 and Nota <= 5:

                    SumaNotas= SumaNotas + Nota #Sumamos notas de los estudiantes
                    break
            except:
                print("Ingrese una nota valida")    

        #print info estudiante
        print("----------------------------------------")
        print("Nombre: {} {}".format(Nombre,Apellido))
        print("Edad: {}".format(Edad))
        print("Nota: {}".format(Nota))
        print("----------------------------------------")

    Promedio= SumaNotas/Estudiantes # promedio de la clase
    #print promedio de notas
    print("Promedio de la clase es: {}".format(Promedio))

SENA()