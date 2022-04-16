
def pizza():

    #Ingredientes extras de pizza
    pepillinos= 2000
    champillones= 2500
    cebollas= 1500

    #suma de ingredientes extras
    sumaPE=0
    sumaCH=0
    sumaCE=0

    #variables tamaños de pizza
    pequeña= 12000
    mediana= 24000
    grande=48000
    sencilla = 3500 #tipos de pizza
    #precio extra
    extra= 1.5

    while(True):

        # !!!!!!! MENU 1 !!!!!!!
        print("----- MENU ----- ")
        print("----- [1] Pequeña ----- ")
        print("----- [2] Mediana ----- ")
        print("----- [3] Grande----- ")
        print("----- [4] SALIR PROGRAMA----- ")
        op=int(input("Ingrese una opcion del menu: ")) # opcion del menu por teclado

        if op== 4:
            break

        if op== 1 or 2 or 3:

            print("Deseas agregar ingredientes extras? ingrese si o no")
            opE = str.lower(input("RTA: ")) # se ingresa por teclado si desea ingredientes extras
            print("-------------------------------------------------------")

            if opE== "si": # Conditional del ingredientes extras

                #Hacemos un ciclo while por si el cliente desea ingresar muchos productos extras
                while(True):

             
                    #Pintamos menu de elegir ingredientes extras
                    # !!!!!!! MENU 2 !!!!!!!
                    print("DESEAS AGREGAR OTRO INGREDIENTE !!")
                    print("----- Ingredientes extras ----- ")
                    print("----- [1] pepinillos ----- ")
                    print("----- [2] champiñones ----- ")
                    print("----- [3] cebollas ----- ")
                    print("----- [0] NO QUIERO AGREGAR INGREDIENTES EXTRAS ----- ")
                    opcion=int(input("Ingrese opcion del menu: ")) #opcion por teclado de ingredientes extras
                    print("-------------------------------------------------------")
                  

                    #conditional del MENU 2
                    if opcion == 1:
                        print("Haz elegido pepinillos!!")
                        print("-------------------------------------------------------")
                        sumaPE= sumaPE + pepillinos # suma de precios extras
                    
                    elif opcion == 2:
                        print("Haz elegido champiñones !!")
                        print("-------------------------------------------------------")
                        sumaCH= sumaCH + champillones # suma de precios extras

                    elif opcion == 3:
                        print("Haz elegido cebollas !!")
                        print("-------------------------------------------------------")
                        sumaCE= sumaCE + cebollas # suma de precios extras
                    
                    elif opcion== 0:
                        print("Gracias por su compra :) ")
                        print("-------------------------------------------------------")
                        break # rompemos CICLO WHILE interno

                if op== 1: # pizza pqueña
                    totalex= (pequeña + sencilla + sumaPE + sumaCH + sumaCE) * extra
                    print("Total de su pizza es: {}".format(totalex))
                    print("-------------------------------------------------------")

                elif op== 2: # pizza mediana
                    totalex= (mediana + sencilla + sumaPE + sumaCH + sumaCE) * extra
                    print("Total de su pizza es: {}".format(totalex))
                    print("-------------------------------------------------------")

                
                elif op== 3: # pizza grande
                    totalex= (grande + sencilla + sumaPE + sumaCH + sumaCE) * extra
                    print("Total de su pizza es: {}".format(totalex))
                    print("-------------------------------------------------------")

            # pizzas sencillas
            elif opE== "no":
                
                if op == 1: #pizza pqueña
                    total= (pequeña + sencilla ) * extra
                    print("total de la pizza es: {}".format(total))
                    print("-------------------------------------------------------")
                
                if op == 2: # pizza mediana
                    total= (mediana + sencilla ) * extra
                    print("total de la pizza es: {}".format(total))
                    print("-------------------------------------------------------")

                if op == 3: #pizza grande
                    total= (grande + sencilla ) * extra
                    print("total de la pizza es: {}".format(total))
                    print("-------------------------------------------------------")
            

pizza()