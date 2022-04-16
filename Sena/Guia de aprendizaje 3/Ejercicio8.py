'''
En cierta empresa se les paga a sus trabajadores de la siguiente forma: si el empleado es de planta,
la hora trabajada se le paga a $20000, si el empleado es administrativo, la hora trabajada se le paga
a $10000. Para calcular su pago es necesario conocer el total de horas trabajadas.

'''

def company():

    #Variables
    EmpleadoPlanta=20000
    EmpleadoHora=10000

    #Print MENU
    print("----- MENU -----")
    print("----- [1] Empleado de planta -----")
    print("----- [2] Empleado por horas -----")
    Op=int(input("Ingrese tipo de empleado: ")) #Variable menu
    Hora=int(input("Ingrese numero de horas trabajadas: ")) # horas trabajadas
    
    #Conditional
    if Op ==1:
        Pago=Hora*EmpleadoPlanta #Calculo horas trabajdas 
        print("Su pago del mes es: {}".format(Pago))

    elif Op==2:
        Pago2= Hora*EmpleadoHora #Calculo horas trabajdas 
        print("Su pago del mes es: {}".format(Pago2))
    
    elif Op <=0 or Op >=3:
        print("Opcion no valida del menu")

company()