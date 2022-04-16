'''
En una tienda de HELADO da un descuento por compra a sus clientes con membresía dependiendo
de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C.
Los descuentos son los siguientes:
Tipo A 10% de descuento
Tipo B 15% de descuento
Tipo C 20% de descuento

'''

def Shop():

    #Varialbe
    Helado=8000
    #Descuentos segun tipo de membresia
    Descuento_A = Helado*0.10
    Descuento_B = Helado*0.15
    Descuento_C = Helado*0.20

    #Pintar menu
    print("----- MENU -----")
    print("----- [A] Tipo A-----")
    print("----- [B] Tipo B-----")
    print("----- [C] Tipo C-----")
    Membresia=str.upper(input("Ingrese una opcion del menu: ")) #Opcion del menu

    #Conditional
    if Membresia =="A": #Membresia tipo A

        Total_A= Helado -Descuento_A
        print("Total a pagar: {}".format(Total_A))
    
    elif Membresia =="B": #Membresia tipo B
        Total_B = Helado -Descuento_B
        print("Total a pagar es: {}".format(Total_B))
    
    elif Membresia == "C": #Membresia tipo C
        Total_C= Helado - Descuento_C
        print("Total a pagar es: {}".format(Total_C))

Shop()

