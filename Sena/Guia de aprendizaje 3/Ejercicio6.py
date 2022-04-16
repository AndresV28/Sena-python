'''
Considere dos variables llamadas temperatura y presión. Escriba una sentencia if-else que muestre
en pantalla la palabra Alarma si la variable presión es mayor a 200 o si la variable temperatura es
mayor a 100. En caso contrario, se debe mostrar en pantalla la palabra Normal.

'''

def Temperature():

    #Variables
    Temperature=float(input("Ingrese valor de la temparatura: "))
    Pressure=float((input("Ingrese valor de la presion: ")))

    #Conditional
    if Temperature > 200 or Pressure >100 :
        print("!!!!! DANGER !!!!! ")
    
    else:
        print("Temperature and pressure are stable")

Temperature()