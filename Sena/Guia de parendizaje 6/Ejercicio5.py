'''
Algoritmo Calcular la factorial de un número N.
'''
# variable num ingresa por valor
def factorial(num):
    #varible
    fac=1
    for i in range (2,(num+1)): #arrancamos el fo de la posicion 2 para comenzar a multiplicar 2*1
        fac= fac * i
    print("El factorial del numero {} es: {} ".format(num,fac)) #print

num=int(input("Ingrese un numero para saber si factorial: ")) # usuario ingresa numero que quiere calcular
factorial(num) #llamado de la funcion