'''
Calcule el mayor de tres números, permitiendo leer 3 valores diferentes
'''

def num():
    #imput variable
    Num1=int(input("Ingrese un numero: "))
    Num2=int(input("Ingrese un numero: "))
    Num3=int(input("Ingrese un numero: "))

    #Conditional 
    if Num1 > Num2 > Num3 : #comparison of numbers
        print("El numero mayor es: {}".format(Num1)) 

    if Num2 > Num1 > Num3 : #comparison of numbers
        print("El numero mayor es: {}".format(Num2)) 

    if Num3 > Num1 > Num2 : #comparison of numbers
        print("El numero mayor es: {}".format(Num3))

num()