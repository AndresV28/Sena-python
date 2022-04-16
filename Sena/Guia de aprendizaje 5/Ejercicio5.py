'''
Un empleado de la tienda “Tiki Taka” realiza N ventas durante el día, se requiere saber cuántas de
ellas fueron mayores a $1000, cuántas fueron mayores a $500 pero menores o iguales a $1000, y
cuántas fueron menores o iguales a $500. Además, se requiere saber el monto de lo vendido en cada
categoría y de forma global. Realice un algoritmo que permita determinar lo anterior.

'''

def ventas():
    #variables mayor a 1000
    mayor=0
    sumaMayor=0
    #variables mayor a 500 o igual a 1000
    media=0
    sumaMedia=0
    #Variables menores o iguales a 500
    bajo=0
    sumaBajo=0
    #Variable total venta
    total=0

    num=int(input("Ingrese numero de ventas realizadas: "))
    for i in range (num):
        venta=int(input("Ingrese venta: "))

        if venta > 1000:
            sumaMayor= sumaMayor + venta
            mayor= mayor +1
        
        elif venta > 500 and venta <= 1000:
            sumaMedia = sumaMedia + venta
            media= media +1
        
        elif venta <= 500 :
            sumaBajo = sumaBajo + venta
            bajo= bajo + 1
    # total de ganancias
    total= sumaMayor + sumaMedia + sumaBajo
    
    #print
    print("ventas mayores a 1000 fueron: {} con un valor total de: {}".format(mayor,sumaMayor))
    print("ventas entre 501 y 1000 fueron: {} con un valor total de: {}".format(media,sumaMedia))
    print("ventas menores a <= 500 fueron: {} con un valor total de: {}".format(bajo,sumaBajo))
    print("------------------------------------------------------------------------------------------")
    print("Total de ganancia: {}".format(total))

ventas()