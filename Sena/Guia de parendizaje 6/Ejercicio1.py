'''
1. Que calcule el gasto de agua en una vivienda dado el número de litros gastados, siendo el sistema
de cobro:
• La cuota fija mensual es de 600 pesos
• Los primeros 50 litros son gratis (opción 1)
• Mayor de 50 y 200 litros se cobra el litro a 1000 pesos (opción 2)
• Mayor de 200 litros se cobra el litro a 3000 pesos (opción 3)
• Indicación: hazlo con tres ‘SI’, uno por cada opción.
'''

# variables entrar por valor
def gasto(litro,cuota):

    #conditional
    if litro<=50:
        print("No pagas el recibo del agua")  #opcion 1
        print("-----------------------------------")

    if litro >50 and litro <=200:
        pago1= (litro * 1000) + (cuota) - 50000
        print("el pago del mes es {}".format(pago1)) #opcion 2
        print("-----------------------------------")

    if litro > 200:
        pago2=( litro * 3000) + (cuota) - 50000
        print("el pago del mes es {}".format(pago2)) #opcion 3
        print("-----------------------------------")
        
while(True):
    #Variable cuotra fija 
    cuota=600

    #pedimos una opcion para arrancar el programa
    op=str.upper(input("Quieres calcular un recibo del agua escriba SI O NO: "))
    #contidional
    if op == "SI":
        litro=float(input("Ingrese litros: ")) # numero de litros
        gasto(litro,cuota) #llamado de la funcion

    elif op == "NO":
        break  #Rompemos ciclo while true
