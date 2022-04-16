'''
Restarle al primer número al segundo (siempre y cuando el primero sea mayor que él segundo, en
caso contrario indicar con un mensaje que la operación no es posible realizarla.
'''

def Resta():
    #Variables
    Num1=int(input("Ingrese numero 1: "))
    Num2=int(input("Ingrese numero 2: "))

    #Conditional
    if Num1 > Num2:
        Resta= Num1 -Num2
        print("{}-{} = {}".format(Num1,Num2,Resta)) #print RESTA
    else:
        print("La operación no es posible realizarla")

Resta()