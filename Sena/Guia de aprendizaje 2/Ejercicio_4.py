'''
 Se recibe un préstamo del banco y desea saber cuánto se pagará de interés mensual, si el banco le 
cobra una tasa del 27% anual.
'''

def prestamo():

    prestamo=float(input("Ingrese cantidad del prestamo: ")) # cantidad del prestamo
    interes= prestamo *0.27 # operancion del interes del prestamos

    total= interes / 12 #total de interes anual

    #imprimir resultado
    print("Total intereses anual es: {}".format(round(total,3))) # interes en el año

prestamo()