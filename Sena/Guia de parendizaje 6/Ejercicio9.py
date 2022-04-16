'''
Diseñe un pseudocódigo que lea el valor de un ángulo expresado en radianes y calcule e imprima el
valor del seno de dicho ángulo. Se leerá también el número de términos de la serie.
SEN(X) = X - ( X 3 / 3 ! ) + ( X 5 / 5 ! ) - (X7/ 7!) + .....
'''
# num entra por valor
def seno(num):

    #Variables
    fac= 1
    lista=[]
    suma1=0
    suma2=0

    for i in range (2,(num+1)):
        fac= fac * i
        if i % 2!=0: # condicional para sacar factorial de numeros impares
            total=(num*i)/fac
            lista.append(total) # agregamos a la lista
      
    #for para recorrer la lista
    for h in range(len(lista)):
        if h % 2 ==0:   # posiciones par de la lista la sumamos
            suma1= suma1 + lista[h]
            
        elif h % 2 !=0: # posicion impares de la lista, la sumamos y dara un numero negativo
            suma2= suma2 + lista[h]
            
        
        final= num + (suma1 - suma2) # restamos la suma positiva y la suma negativa
    
    print("El seno es: {}".format(round(final,3)))

num=int(input("Ingrese un numero: ")) # numero de veces que se va repetir el ciclo
seno(num) #llamado del metodo