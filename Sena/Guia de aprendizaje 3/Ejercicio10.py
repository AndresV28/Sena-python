'''
Calcular el valor total del valor de 5 productos, el IVA y el subtotal, visualizar los resultados de:
Iva, Subtotal y Total de la compra de los artículos.

'''

def productos():

    #Variables
    SumaTotal=0
    SumaIva=0
    SubTotal=0

    for i in range(5):
        precio=float(input("Ingrese el valor del producto {}: ".format(i+1)))

        #conditional
        if precio > 0:

            #TOTAL SIN IVA 
            SumaTotal= SumaTotal + precio

            #IVA
            iva= precio * 0.19 #iva colombiano
            SumaIva= SumaIva + iva # suma total del iva de los 5 productos

            #Total de producto con iva
            TotalProducto = precio + iva 
            
            #Precio final
            SubTotal = SubTotal + TotalProducto
        
        else:
            print("El producto tiene un valor de 0 pesos")

    #print
    print("-----------------------------------------------------")
    print("Total de los productos sin IVA: {}".format(SumaTotal))
    print("IVA de los productos: {}".format(SumaIva))
    print("TOTAL A PAGAR: {}".format(SubTotal))

productos()