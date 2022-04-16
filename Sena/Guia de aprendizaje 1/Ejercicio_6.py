'''
6)Escribir un programa que calcule el volumen de una esfera:
Radio = 3 volumen de la esfera = 4/3 * PI * radio˄3
'''

def volumen():
    # VARIABLES
    pi= 3.1416;
    radio=3;

    volumen= (4/3) * (pi * pow(radio,2)); # VOLUMEN DE UNA ESFERA

    print("El volumen de la esfera es: {} ".format(round(volumen,2))); #PRINT DEL RESULTADO
volumen()
