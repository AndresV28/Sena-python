'''
8)Escribir un programa que calcule el área y el volumen de un cilindro:
A = (2 * (PI * r˄2)) + ((2 * PI * r) * h)
V = (PI * r2) * h
'''

def cilindro():
    #VARIABLES
    pi= 3.1416;

    #INPUT
    r=float(input("Ingrese radio del cilindro: "));
    h=float(input("Ingrese alura del cilindro: "));

    # AREA Y VOLUMEN DEL CILINDRO
    A = 2 *(pi * r**2) + (2 * pi * r) * h;
    V = (pi * r**2) * h;

    # PRINT RESULTADO 
    print("El area del cilindro es: {}".format(A));
    print("El volumen del cilindro es: {}".format(V));

cilindro()

