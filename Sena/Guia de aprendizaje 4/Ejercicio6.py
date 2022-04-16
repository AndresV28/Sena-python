'''
Realice un Algoritmo que permita calcular y dar como salida el promedio de bateo (PB) de cada
jugador perteneciente a un equipo de 10 jugadores, tomando en cuenta que se tienen los siguientes
datos:
• Nombre del Jugador
• Veces al Bate (VB)
• Hit Conectados (HIT)
• Extrabases Conectadas (EXT)
• Cantidad de Sacrificios (S)
• Cantidad de Bases por Bolas Recibidas (BB)
NOTA:
PB = BBC / VLB * 1000 donde:
BBC = HIT + EXT
VLB = VB – S – BB

'''

def Bateo():
    
    num=int(input("Ingrese numero de jugadores que desea promediar: "))
    #variable
    x=0
    promedio=0
    #ciclo
    while (x <num):

        nombre=str.upper(input("Ingrese Nombre del jugador {}: ".format(x+1))) #nombre jugador
        Bateo=int(input("Ingrese numeros de veces al bate: ")) #Veces al Bate (VB)
        Hit=int(input("Ingrese numero de hit conecatods: ")) # Hit Conectados (HIT)
        extraB=int(input("Ingrese numero de extra bases conectadas: ")) #Extrabases Conectadas (EXT)
        Sacrificios=int(input("Ingrese numero de safricios: ")) #Cantidad de Sacrificios (S)
        Bases=int(input("Ingrese numero de bases por bolas: ")) #Bases por Bolas Recibidas (BB)

        
        BBC = Hit + extraB # (HIT) * (EXT)
        VLB= Bateo - Sacrificios - Bases  #(VB) - (S) - (BB)

        if VLB > 0 :
            PB = (BBC / VLB) * 1000 #promedio

            x=x+1 # contador para romper ciclo
            promedio= (promedio + PB)/num #promedio total del equipo 

            print("El promedio del jugardor #{} {} es: {}".format(x,nombre,PB)) #promedio por jugador
            print("---------------------------------------------------------")
        else:
            print("haz ingresado datos errores !!! ")

    print("Promedio total de bateo del equipo es: {}".format(promedio)) # promedio del equipo 

Bateo()

