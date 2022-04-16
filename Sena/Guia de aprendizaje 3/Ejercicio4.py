'''
Cálculo de áreas - Elige una figura geométrica:" Triángulo y Círculo
¿Qué figura quiere calcular (Escriba T o C)?
Triangulo = base * altura / 2
Circulo = PI * radio* radio

'''
import math

def areas():

    print("----- MENU -----")
    print("----- [T] Area del triangulo -----")
    print("----- [C] Area del circulo-----")
    print("-------------------------------------")
    Letra =str.upper(input("Ingrese una opcion del menu: "))

    if Letra == "T" :
        Base= float(input("Ingrese Base del tritnagulo: "))
        Altura=float(input("Ingrese altura del triangulo: " ))

        Triangulo=Base * Altura / 2

        print("El area del triangulo es: {}".format(round(Triangulo,2)))

    elif Letra == "C":
        pi= math.pi
        radio=float(input("Ingrese radio del crculo: "))

        Circulo = pi * radio* radio

        print("El area del circulo es: {}".format(round(Circulo,2)))

areas()

