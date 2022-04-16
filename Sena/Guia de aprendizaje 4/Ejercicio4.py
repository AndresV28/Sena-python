'''
Desarrolle un programa que invierta un número entero N dado por el usuario. Por ejemplo, de 12345
su número invertido es 54321.

'''

from ntpath import join


def invertir():

    while(True):
        
        Num=int(input("Ingrese un numero a convertir: ")) # pedidos dato por teclado

        Num = str(Num) #Convertidos un entero a string

        print("".join(reversed(Num))) #join pone el string en una fila de carecteres y reverse invierte el string
                                      
        if Num==0 :
            break #rompemos ciclo si ponen un numero 0
        

invertir()