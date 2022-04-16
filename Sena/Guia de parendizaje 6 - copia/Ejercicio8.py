'''
Diseñe un algoritmo que determine el resultado de la elección del representante estudiantil de la
universidad X, para ello se presentaron tres candidatos A, B, y C.
• Para ganar la elección se debe obtener como mínimo el 51%.
• En caso que no haya un ganador se repite la elección en una segunda vuelta.
• Van a la segunda vuelta los dos candidatos que obtengan la más alta votación.
• Se anula la elección en caso de producirse un empate doble por el segundo lugar o un empate
triple.
'''

#No ingresar ningun valor a la funcion
def eleccion():
    #variables
    contador1=0
    contador2=0
    contador3=0
    lista=[]  # lista para guardar los votos

    while(True): # usamos while para pedir votos infinitos 
        voto=int(input("Ingrese su voto: "))
        #conditional
        if voto > 0 and voto <4:
            lista.append(voto) # agregamos votos a la lista
        
        else:
            break # rompemos ciclo while true si no se cumple la condicion de los votos

    encuesta(lista,contador1,contador2,contador3) # enviados datos por valor a la funcion

#INPUT datos por valor de la funcion ----> seleccion()
def encuesta(lista,contador1,contador2,contador3):

    for i in range(len(lista)): # usamos for para recorrer la lista y hacemos comparativa de votos
        #conditional para sumar los votos por medio de contadores
        if lista[i]== 1:
            contador1+=1 #Representante A

        elif lista[i]== 2: #Representante B
            contador2+=1

        elif lista[i]==3: #Representante C
            contador3+=1
    
    totalvotos= contador1 + contador2 +contador3 #total de votos
    comparativa = (totalvotos/2)+1 #guardamos este resultado para saber si hay algun ganador con el 51 de los votos

    # ----------- RESULTADOS SI ALGUIEN GANA EN LA PRIMERA VUELTA -----------
    #GANADOR A
    if contador1 > contador2 and contador1 > contador3:
        if contador1 > comparativa:
            print("El represententate A es el ganador")
    
    #GANADOR B
    elif contador2 > contador1 and contador2 > contador3:
        if contador2 > comparativa:
            print("El represententate B es el ganador")

    #GANADOR C
    elif contador3 > contador1 and contador3 > contador2:
        if contador3 > comparativa:
            print("El represententate C es el ganador")

    #  VEMOS QUIEN PASA A LA SEGUNDA VUELTA SI NO HAY GANADOR EN PRIMERA VUELTA
    
    #si el numero el 51% de los votos supera a todos los candidatos
    if comparativa > contador1 and comparativa > contador2 and comparativa > contador3:
        print("No hubo ganador en la primera vuelta")
        
        if contador1 and contador2 > contador3 : # avanzan A Y B
            print("Candidato A avanza con {} votos y candidato B avanza con {} votos".format(contador1,contador2))
        
        elif contador1 and contador3 > contador2 :  # avanzan A Y C
            print("Candidato A avanza con {} votos y candidato C avanza con {} votos".format(contador1,contador3))

        elif contador2 and contador3 > contador1 :  # avanzan B Y C
            print("Candidato B avanza con {} votos y candidato C avanza con {} votos".format(contador2,contador3))
        
        elif contador3 and contador2 > contador1 :  # avanzan C Y B
            print("Candidato C avanza con {} votos y candidato B avanza con {} votos".format(contador3,contador2))
        


eleccion() # funcion primera vuelta

#ingresan datos por valor
def segunda(contador4,contador5):
    while(True):

        voto2=int(input("Ingrese su voto de segunda vuelta: ")) # usuario ingresa su voto
        if voto2 >0  and voto2 <3:
            if voto2 == 1:  #representante A
                contador4+=1

            elif voto2 == 2: #representante B
                contador5+=1
        else:
            break
    #conditional para saber el ganador 
    if contador4 > contador5:
        print("Repensente A gana las elecciones con {} votos ".format(contador4)) #representante A
    else:
        print("Repensente B gana las elecciones con {} votos ".format(contador5)) #representante B

#variable contadoras

contador4=0
contador5=0
opcion=str.upper(input("desea comenzar la segunda vuelta SI O NO: "))
if opcion=="SI":
    segunda(contador4,contador5) # llamado de la segunda funcion para segunda vuelta

else:
    pass










        
