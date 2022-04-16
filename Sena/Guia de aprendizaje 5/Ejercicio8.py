'''
Hacer un algoritmo que al ingresar N números por la pantalla y se calcule la suma, resta,
multiplicación y división. El proceso debe terminar cuando se hallan realizado 10 procesos (Hacer uso
de contadores).

'''

def matematicas():
    #varibles
    suma=0
    resta=0
    multi=1
    div=0
    #ciclo
    for i in range (3):
        num=int(input("Ingrese un numero: ")) #usuario ingresa numeros
        #operaciones
        suma = suma + num  #suma

        if i==0:
            resta= num  #le doy valor directo a la division y resta para que comiencen en un numero positivo
            div = num   # y no arranque de forma negrativa para restar y dividir
        if i >0:
            resta = resta -num  #En este bloque ya se hacen las operaciones normalmente
            div = div / num

        multi = multi * (num)  # multiplicacion
       
    #print
    print("---------------------------")  
    print("Total suma: {}".format(suma))
    print("Total resta: {}".format(resta))
    print("Total multiplicacion: {}".format(multi))
    print("Total division: {}".format(div))

matematicas()