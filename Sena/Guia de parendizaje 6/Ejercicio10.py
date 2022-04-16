'''
Crear un programa que registre 50 números enteros y luego muestren los elementos que son
múltiplos de 5, este se determina si con la fórmula de: Numero_ingresado_porteclado mod = 0.
'''
#variable entra por valor
def multiplos(contador):

    for i in range(1,1000):

        if i % 5 == 0:  # si residuo de una division por 5 es 0 entonces es multiplo
            print("Numero {} es multiplo de de 5 ".format(i))
            contador = contador + 1 #contador paara cuando lleguen 50 numero rompa el ciclo
        
        if contador == 50:
            break  # rompemos ciclo for

#variable        
contador=0 
multiplos(contador) #llamado de la funcion