'''
Realizar el algoritmo que lea N números, calcule y escriba la suma de los pares y el producto de los
impares. Numero par es aquel que su residuo igual a cero (num mod !=0)

'''

def sum():
    #Varialbes
    SumaPar=0
    SumaImpar=0
    close=0
    
    #cicle
    while(close >= 0):
        num=int(input("Ingrese un numero entero: "))

        #Conditional
        if num <0:
            close=num
            break #Rompemos ciclo while(mientras)

        if num % 2 == 0 : #Residuo de la division si es cero es un numero par
            SumaPar = SumaPar + num
            
        else:
            SumaImpar = SumaImpar + num

    # print
    print("La suma de los numero PARES es: {}".format(SumaPar))
    print("La suma de los numero IMPARES es: {}".format(SumaImpar))
        
sum()