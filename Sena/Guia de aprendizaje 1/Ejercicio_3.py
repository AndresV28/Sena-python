'''
3) Un programa que lea 4 números y calcule la media.
Media= (num1 + num2 + num3 + num4)/4
'''

def Media():
    #VARIABLE
    suma=0;
    # CICLO FOR
    for i in range(4):
        num=float(input("Ingrese numero {}: ".format(i+1) ));
        suma= suma + num; # SUMA DE NOTAS

    promedio= suma/4; # PROMEDIO DE NOTAS
    
    print("Promedio de los numero es: {}".format(promedio)); # PRINT RESULTADO
Media()

