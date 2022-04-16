'''
10) Una farmacia aplica al precio de los remedios el 10% de descuento, hacer un programa que
ingresando el costo de los medicamentos calcules el descuento y el precio final.
'''

def farmacia():
    #INPUT
    obj = int(input("Ingrese valor del producto: "));

    #OPERACIONES MATEMATICAS
    descuento= (obj * 0.1);
    precio= obj - descuento ;

    #PRINT RESULTADO
    print("Total a pagar es: {}".format(precio))
    
farmacia()

