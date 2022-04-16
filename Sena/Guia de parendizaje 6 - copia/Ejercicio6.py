'''
Construya los algoritmos que permitan calcular las siguientes series con un valor de N ingresado
desde teclado:
1**2+ 2**2 + 3**2 +...N2 tal que N es positivo

1**1 + 2**2 + 3**3+...Nn tal que N es positivo
'''
#variable op ingresa por valor
def algoritmos(op):
    #variables
    suma=0
    suma2=0

    for i in range(1,op+1):
        #1**2+ 2**2 + 3**2 +...N
        total1=i**2  # elevamos 
        suma = suma + total1 # sumamos resultados

        #-----------------------------------
        
        #1**1 + 2**2 + 3**3+...N
        total2= i**i
        suma2= suma2 + total2

        
    print("la suma de 1**2+ 2**2 + 3**2 +...N es: {}".format(suma))
    print("------------------------------------------------------")
    print("la suma de 1**1 + 2**2 + 3**3+...N es: {}".format(suma2))

op=int(input("Ingrese numero que sea desea calcular n veces: ")) # numero de veces que vamos a repetir ciclo
algoritmos(op) # llamdo de la funcion