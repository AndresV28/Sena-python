'''
En un club se registran de uno en uno los siguientes datos de sus socios: Documento de socio,
Apellido y nombre, Edad y Tipo de deporte que practica (1 tenis, 2 rugby, 3 voley, 4 hockey, 5 futbol).
Diseñar el código de un algoritmo que permita mostrar por pantalla cuantos socios practican cada
deporte y el promedio de edad de los jugadores.

'''

def deportes():
    #variables de numero de socios
    tenis=0
    rugby=0
    voley=0
    hockey=0
    futbol=0
    #variblaes de suma de edades para promedio 
    sumaEdad =0
    sumaEdadR=0
    sumaEdadV=0
    sumaEdaH=0
    sumaEdaF=0

    #ciclo
    while(True):
        documento=int(input("Ingrese documento del socio: "))
        if documento < 0:
            break # rompemos cicli con un numero negativo

        apellido=str(input("Ingrese apellido del socio: "))
        nombre=(str(input("Ingrese nombre del socio: ")))
        deporte= int(input("Ingrese deporte que practica: "))
        edad= int(input("Ingrese edad: "))
        print("---------------------------------")
    
        #conditional

        if deporte==1:
            tenis = tenis +1 #Contador de socios
            sumaEdad = sumaEdad + edad # suma de edades de los socios
        
        elif deporte == 2:
            rugby = rugby +1 #Contador de socios
            sumaEdadR = sumaEdadR + edad # suma de edades de los socios

        elif deporte == 3:
            voley= voley +1 #Contador de socios
            sumaEdadV = sumaEdadV + edad # suma de edades de los socios

        elif deporte == 4:
            hockey = hockey +1 #Contador de socios
            sumaEdadH = sumaEdaH + edad # suma de edades de los socios

        elif deporte == 5:
            futbol = futbol +1 #Contador de socios
            sumaEdadF = sumaEdaF + edad # suma de edades de los socios

    
    #tenis
    if tenis > 0:
        print("----------------------------------------------------------------")
        print("Numero de socios que juegan tenis es: {}".format(tenis)) # numero de socios
        print(f"promedio de la edad de jugadores de tenis es: {sumaEdad/tenis} ") #promedio edad
    else:
        print("Numero de socios que juegan tenis es: {}".format(tenis))   
    print("----------------------------------------------------------------")

    #rugby
    if rugby > 0:
        print("Numero de socios que juegan rugby es: {}".format(rugby)) # numero de socios
        print(f"promedio de la edad de jugadores de rugby es: {sumaEdadR/rugby} ") #promedio edad
    else:
        print("Numero de socios que juegan rugby es: {}".format(rugby))
    print("----------------------------------------------------------------")

    #voley
    if voley > 0:
        print("Numero de socios que juegan voley es: {}".format(voley)) # numero de socios
        print(f"promedio de la edad de jugadores de voley es: {sumaEdadV/voley} ")#promedio edad
    else:
        print("Numero de socios que juegan voley es: {}".format(voley))
    print("----------------------------------------------------------------")

    #hockey
    if hockey > 0:
        print("Numero de socios que juegan hockey es: {}".format(hockey)) # numero de socios
        print(f"promedio de la edad de jugadores de hockey es: {sumaEdadH/hockey} ")#promedio edad
    else:
        print("Numero de socios que juegan hockey es: {}".format(hockey))
    print("----------------------------------------------------------------")

    #futbol
    if futbol > 0:
        print("Numero de socios que juegan utbol es: {}".format(deporte)) # numero de socios
        print(f"promedio de la edad de jugadores de futbol es: {sumaEdadF/futbol} ")#promedio edad
    else:
        print("Numero de socios que juegan  futbol es: {}".format(futbol))
    print("----------------------------------------------------------------")

deportes()
