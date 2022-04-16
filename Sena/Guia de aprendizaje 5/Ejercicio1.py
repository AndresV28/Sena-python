'''
Escribe la tabla de multiplicar de un numero N positivo.

'''

def Multiplicaicon():
    #ciclo while para programa infinito
    while(True):
        op=str.lower(input("Desea realizar una multiplicacion, indique si o no: ")) #opcion de los condicionales
        #Conditional
        if op == "si" :
            
            num=int(input("Ingrese un numero positivo para saber su tabla de multiplicar: "))
            for i in range(1,11): # ciclo for que recorre 10 veces 
                resultado = num * i
                print("{} * {} = {}".format(num,(i),resultado))

        elif op== "no":
            print("Gracias por usar nuestro programa")
            break
 
Multiplicaicon()