'''
Realizar un algoritmo que dado un numero definido de notas, me permita calcular el promedio
'''

def promedio():
    promedio=0 # variable de sumatoria de notas
    notas=int(input("Ingrese numero de notas: ")) # numero de notas a ingresar por teclado

    for i in range(notas): # range(nota)--> va hacer el ciclo las veces del numero de notas
 
        while(True): # ciclo while con execpcion para error humano y no ingrese notas mayores a 5
            try:
                nota=float(input("Ingrese nota {}: ".format(i + 1))) # nota ingresesada por teclado
                #condicional 
                if nota<=5:
                    promedio= (promedio + nota)
                    break # rompemos ciclo while y entra nuevamente el FOR
                else:
                    print("Ingrese una nota menor a 5 y mayor a 0")
            except:
                break

    notaF= promedio / notas # operacon de promedio de notas
    #imprimir 
    print("Nota final es: {} ".format(notaF))
promedio()