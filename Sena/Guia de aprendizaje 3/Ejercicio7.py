'''
Calcular todos los pagos hechos de un restaurante y que si el consumo ingresado excede los
$130.000 el descuento será del 15%, de lo contrario no hay descuento.
'''

def Restaurant():

    #Variables
    Bill=float(input("Ingrese Valor de la factura: "))

    #Conditional
    if Bill > 130000:
        Discount= Bill * 0.15 #Descuento del 15%
        Total= Bill -Discount #Restamos el descuento del precio original
        print("Total a pagar: {}".format(Total))
    
    else:
        print("Total a pagar es: {}".format(Bill))

Restaurant()