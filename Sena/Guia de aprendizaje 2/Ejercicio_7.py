'''
Realice un algoritmo que a partir de proporcionarle la velocidad de un automóvil, expresada en 
kilómetros por hora, proporcione la velocidad en metros por segundo. calculo= (Velocidad_automovil)* 
1000) / 3600
'''

def velocidad():

    velocidad=int(input("Ingrese velocidad: ")) # Velocidad en km cuadrados
    calculo= (velocidad* 1000) / 3600 #calculo de velocidad en metros por segundos

    #Imprimir
    print("La velocidad del vehiculo en metros por segundo: {}" .format(round(calculo,3)))
       
velocidad()