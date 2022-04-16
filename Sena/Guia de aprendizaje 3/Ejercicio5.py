'''
Escriba un algoritmo que calcule el área de un rectángulo siempre y cuando los lados sean positivos:
área triangulo= lado * lado.

'''

def Rectangle():

    #Varibles
    Height=float(input("Ingrese altura del rectangulo: "))
    Base=float(input("Ingrese base del rectangulo: "))

    #Conditional
    if Height >0 and Base > 0:
        Rectangle= Height * Base

        print("El area del del rectangulo es: {} ".format(round(Rectangle,2)))  # print resultado

    else:
        print("Por favor ingreser valores mayor a cero")
        
Rectangle()


