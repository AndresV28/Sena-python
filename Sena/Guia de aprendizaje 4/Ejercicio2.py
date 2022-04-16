'''
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se
desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el
ingreso de datos cuando el usuario ingrese el monto 0.
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al
finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $10000,
se le debe aplicar un 10% de descuento.

'''

def compras():

    #variables
    Suma=0 #suma de los productos

    #ciclos
    while(True):

        Monto=float(input("Ingrese monto de la compra: ")) #input por teclado
        
        #contidional  suma de productos
        if Monto==0:
            break

        elif Monto >0:  # si monto es mayor a cero suma el monto

            Suma= Suma + Monto # suma monto

            if Monto < 0:  #si no es mayor a cero rompe condicional y vuelve al while
                print("")


    #conditional de descuento 
    if Suma > 10000:
        
        Descuento = Suma * 0.10

        Total= Suma - Descuento
        print("El total con descuento es: {}".format(Total))

    elif Suma <= 10000:
        print("El total sin descuento es: {}".format(Suma))
            
compras()
