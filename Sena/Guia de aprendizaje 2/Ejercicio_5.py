'''
Calcular el total de la suma de todas las compras en una variable de tipo decimal, luego se calcula 
los descuentos de un 2.5% y se muestra el total a pagar incluyendo los impuestos del 11%.
'''
def compras():
    total=0 # variable de sumas de compras
    x=0
    contador=1

    while(True):
        try:
            confir=int(input("Ingrese numero de compras: "))
            break       
        except:
            print("Ingrese un valor numerico")
            print("==========================")

    while confir > x :   
        
        compra=float(input("Ingrese su compra {} :".format(contador)))
        total= total + compra
        x=x+1 # break del while
        contador = contador + 1 # contador para ver el numero de las compras 


    descuento = total * 0.025 # descuento de la compra
    impuestos= total * 0.11 # impuestos
    totalFinal= (total - descuento) + impuestos # total a pagar, se hace el descuento y luego se le suma el impuesto
    
    #Imprimir
    print("=========================================")
    print("Valor neto de la compra: {}".format(total))
    print("Descuento de la compra:  {}".format(descuento))
    print("Impuesto de la compra:   {}".format(impuestos))
    print("Total a pagar es: {}".format(totalFinal))
  
compras()