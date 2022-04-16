'''
11. Diseñe un algoritmo que genere los 50 primeros números de la serie Fibonacci.
'''
# num ingresa por valor
def fibonacci(num):
    #variables
    primero=0
    segundo=1
    sum=0
    contador=1
    #ciclo while
    while(contador<=num):    
        print(sum, end="  ") # imprimimos la seir
        primero=segundo # con esta parte comenzamo la secuencia (1)
        segundo=sum
        sum=primero+segundo

        contador = contador + 1 # contador para romper ciclo

num=int(input("ingrese cantidad de numero que quiere ver en la serie ")) # cantidad de numero que quiere ver la serie
fibonacci(num) #llamado de la funcion