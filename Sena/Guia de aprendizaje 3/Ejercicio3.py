'''
Desarrollar un diagrama que lea 3 valores diferentes e indique cual es el mayor de ellos, el menor o
si son iguales.
'''

def num():

    #imput variable
    Num1=int(input("Ingrese un numero: "))
    Num2=int(input("Ingrese un numero: "))
    Num3=int(input("Ingrese un numero: "))

    if Num1 == Num2 == Num3:
        print("todos los numeros son iguales")

#primer numero
    elif Num1 > Num2 > Num3 :
        print("El numero mayor es {}".format(Num1))

        if Num2 > Num3:
            print("El numero menor es {}".format(Num3))
        else:
            print("El numero menor es {}".format(Num2))

#segundo numero
    elif Num2 > Num1 > Num3 :
        print("El numero mayor es {}".format(Num2))

        if Num1 > Num3:
            print("El numero menor es {}".format(Num3))
        else:
            print("El numero menor es {}".format(Num1))
            
#tercer numero
    elif Num3> Num1 > Num2 :
        print("El numero mayor es {}".format(Num3))

        if Num2 > Num1:
            print("El numero menor es {}".format(Num1))
        else:
            print("El numero menor es {}".format(Num2))
   
num()