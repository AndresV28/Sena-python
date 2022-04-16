'''
5)Escribir un programa que calcule la longitud y el área de una circunferencia: Radio = 4
Longitud de la circunferencia = 2 * PI * radio
Área de la circunferencia = PI * radio˄2
'''

from re import match

def circulo():
    #VARIABLES
    radio= 4;
    pi=3.1416;

    #OPERACIONES ARITMETICAS 
    perimetro = 2 * (pi * radio);
    area= (pi* pow(radio,2));
    
    #PRINT DEL RESULTADO 
    print("El perimetro del circulo es: {}".format(perimetro));
    print("El are del circulo es: {}".format(area));

circulo()
