'''
Realizar el siguiente juego: Piedra, papel o tijeras Este es un juego muy antiguo en el que intervienen
dos personas. Cada jugador hace su elección entre las tres alternativas existentes (piedra, papel o
tijeras) y el ganador se determina atendiendo a las siguientes reglas:
• La piedra gana a las tijeras (puede golpearlas hasta romperlas).
• Las tijeras ganan al papel (pueden cortarlo).
• El papel gana a la piedra (puede envolverla).
• Si las dos elecciones son la misma se produce un empate.

'''

import random

#variables entrar por valor
def juego(op,numero):

    print("Vamos a jugar piedra papel o tijera")
    
    # opcion del jugador PIEDRA
    if op < 2 and op < 3:
        if numero == 2:
            print("----- FELICIDADES -----")
            print("piedra le gana a tijera !!! TU HAS GANADO !!! ")
            print("----------------------------------------------")
        else:
            print("----- MALA SUERTE -----")
            print("piedra no le gana a papel !!! TU HAS PERDIDO ")
            print("----------------------------------------------")

    #opcion del jugador tijera
    if op > 1 and op < 3:
        if numero == 1:
            print("----- MALA SUERTE -----")
            print("tijera no le gana a piedra !!! TU HAS PERDIDO ")
            print("----------------------------------------------")
        else:
            print("----- FELICIDADES -----")
            print("tijera le gana a papel !!! TU HAS GANADO !!! ")
            print("----------------------------------------------")

    #opcion del jugador papel
    if op > 1 and op <4:
        if numero== 1:
            print("----- FELICIDADES -----")
            print("papel le gana a piedra !!! TU HAS GANADO !!! ")
            print("----------------------------------------------")
        else:
            print("----- MALA SUERTE -----")
            print("papel no le gana a tijera !!! TU HAS PERDIDO ")
            print("----------------------------------------------")
    #opcion empate
    if op == numero:
        print("Es un empate!!!")
        print("----------------------------------------------")

#Ciclo infinito para jugar hasta que la persona no quiera jugar mas
while(True):
    #pintamos un menu de opciones
    print("-------- MENU --------")
    print("----- [1] piedra -----")
    print("----- [2] tijera -----")
    print("----- [3] papel ------")
    print("----- [0] Terminar programa ------")

    op=int(input("Jugador  ingrese una opcion: ")) #jugador ingresa opcion por teclado
    numero= random.randint(1, 3) #importador clase random para generar un numero aleatorio 
    juego(op,numero) #llamamos a la funcion

    if op == 0: # rompemos ciclo si usuario ingresa cero
        break

