'''
7)Escribir un programa que evalúe la siguiente expresión:
(a+7*c)/(b+2-a)+2*b
'''

def exp():
    # ENTRADAS DE VARIABLES 
    a=int(input("Ingrese valor de A: "));
    b=int(input("Ingrese valor de B: "));
    c=int(input("Ingrese valor de C: "));

    resultado = (a+7*c)/(b+2-a)+2*b; # OPERACION MATEMATICA
    #PRINT DEL RESULTADO
    print("Resultado: {}".format(round(resultado,2)));

exp()

