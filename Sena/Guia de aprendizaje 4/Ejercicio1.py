'''
Realiza un programa en Python, que pida números mientras no se ingrese uno negativo. Al final, se
debe mostrar la suma de los números ingresados.

'''
def num():

    #Variables
    Contador=0
    Suma=0

    while (Contador == 0): 
        Num=int(input("Ingrese un numero: ")) #Usuarui ingresa numero por teclado

        #conditional
        if Num < 0:
            Contador = Num # Cambiamos valor del contador para romper ciclo
  
        else:
            Suma= Suma +Num #Suma de todos los numeros

    #print
    print("La suma de los numeros ingresados es: {} ".format(Suma))

num()