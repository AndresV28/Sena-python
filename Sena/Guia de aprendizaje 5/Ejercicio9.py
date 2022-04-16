'''
Diseñar un diagrama que permita emitir la factura correspondiente a una compra de un artículo del
cual se adquiere una o varias unidades y se conoce su precio antes de IVA (iva igual al 16%), y si el
precio bruto (precio de venta más IVA) es mayor de $500.000.oo se debe realizar un descuento del
15%.

'''
def factura():
    suma=0
    iva=0.16

    cantidad=int(input("Ingrese cantidad de productos a comprar: ")) # condicion para arrancar for
    producto=float(input("Ingrese precio del producto: ")) # pedimos por teclado precio del producto
    InfoIva= producto*iva # sacamos iva del precio del producto
    total = producto + InfoIva # sumamos iva al precio original 
    #for
    for i in range(cantidad): 

        suma= suma + total # sumamos el mismo producto n cantidad de veces
    #conditional 
    if suma > 500000:
        descuento= suma * 0.15  # sacamos valor del descuento
        descuentoFinal= suma - descuento # restamos el descuento al precio original (suma)
        print("---------------------------------------------------------")
        print("subtotal: {}".format(suma))
        print("Total a pagar con descuento es: {}".format(descuentoFinal))  # print final
    
    else:
        print("---------------------------------------------------------")
        print("Total a pagar: {}".format(suma))  # print final
    

factura()

