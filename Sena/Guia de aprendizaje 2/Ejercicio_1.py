
'''
Elabora un algoritmo que permita ingresar el número de partidos ganados, perdidos y empatados por 
algún equipo apertura, se debe mostrar su puntaje total teniendo en cuenta que por cada partido 
ganado obtendrán 3 puntos, empates 1 punto y perdidos 0 puntos.

'''

def partidos():

    #Pedidos los resultados de los partidos

    ganados=int(input("Ingrese numero de partidos Ganadados: "))
    empatados=int(input("Ingrese numero de partidos Empatados: "))
    perdidos=int(input("Ingrese numero de partidos Perdidos: "))

    # Suma de puntos del equipo
    resultado= (ganados*3)+(empatados)+(perdidos) #no es necesario poner los perdidos ya que equivale a 0 puntos
    npartidos= ganados+empatados+perdidos # Total partidos jugados

    #Imprimir reusltados 
    print("Total de puntos del equipo en la temporada es: {} "(resultado))# total puntos de la temporada
    print("Se jugaron un total de : {} partidos en esta temporada ".format(npartidos))# numero de partidos jugados

partidos()
  
