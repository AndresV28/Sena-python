'''
Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos. 
Desarrolle el algoritmo correspondiente.

'''

import math

def hipotenusa():

    #Pedimos los catetos 
    CatetoA= float(input("Ingrese cateto A: "))
    CatetoB= float(input("Ingrese cateto B: "))

    result= CatetoA**2 + CatetoB**2 # teorema de pitagoras  h**2 = a**2 + b**2 - omitimos la hipotenusa al cuadrado

    rHipotenusa = math.sqrt(result) #Importamos clase match y usas sqrt que es la raiz

    #Imprimir
    print("Hipotenusa: {} ".format(round(rHipotenusa,3)))

hipotenusa()