'''
Lorena organiza una fiesta en la cual una computadora controla el ingreso mediante 5 claves. Si se
ingresa al menos una clave incorrecta esta imprimirá "TE EQUIVOCASTE DE FIESTA" y no permitirá
el ingreso. Si las 5 claves son correctas imprimirá "BIENVENIDO A LA FIESTA"
Las Claves son:
1: "TIENES"
2: "QUE SER"
3: "INVITADO"
4: "PARA"
5: "INGRESAR"
'''
#lista entra por valor
def fiesta(lista):
    #variables contadoras
    contador=0 
    x=0
    #while para el numero de intentos 
    while (x<5):
        clave=str.upper(input("Ingrese clave: ")) #clave que ingresa el usuario
        
        bandera = True #creamos bandera para cuando sea flase romper ciclo while si el usuario se equivoca
        for i in range(len(lista)): # recorremos lista que entra por valor
           #conditional 
            if clave == lista[i]:
                contador = contador + 1 #contador de claves acertadas
            
            if clave not in lista: # si la clave no esta en la lista cambiamos valor de bandera 
                bandera= False

        if bandera== False:  #si bandera el flase rompemos ciclo while
            print("TE EQUIVOCASTE DE FIESTA ")
            break
        
        if contador== 5: # contidional para ver si puedes ingresar a la fiesta 
            print("CONTRASEÑAS CORRECTAS")
            print("-----------------------------------")
            print(" !!! BIENVENIDO A LA FIESTA OME OME OME !!! ")
        
        x=x+1 # contador del ciclo while
        

lista=["TIENES","QUE SER","INVITADO","PARA","INGRESAR"] #lista con valores predeterminados
fiesta(lista) #llamado de la funcion
