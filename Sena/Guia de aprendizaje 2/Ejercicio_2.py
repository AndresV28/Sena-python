'''
Hacer un algoritmo dónde una persona recibe un préstamo de $100.00 de un banco y desea saber 
cuánto pagará de interés, si el banco le cobra una tasa del 2% mensual. Ingresar el número de meses 
por teclado.

'''

def prestamo():

    prestamo=100.00 # prestamo realizado
    interes= prestamo* 0.02 # sacamos interes del prestamo 

    meses=int(input("Ingrese numero de meses para conocer su interes: "))
    resultado= (meses*interes)   #Operacion de los interes por meses ingresados

    #Imprimir resultado 
    print("Su interes del prestado de {} en {} meses es: {}".format(prestamo,meses,resultado))

prestamo()