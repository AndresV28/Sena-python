'''
Determinar si un número es positivo y menor que 100.
'''

def num():

    num= int(input("Ingrese un numero: ")) # input variable 

    #conditional and print
    if num > 0 and num< 100:
        print("EL numero {} es positivo y menor de 100 ".format(num))
    else:
        print("El numero {} no esta en el rango de 100 ".format(num))

num()