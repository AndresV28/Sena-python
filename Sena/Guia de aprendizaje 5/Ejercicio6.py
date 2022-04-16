'''
En una empresa de 100 trabajadores, se hará un aumento al salario de acuerdo al tiempo de servicio,
para este aumento se tomará en cuenta lo siguiente:
- Tiempo de servicio: de 1 a 5 años Aumento: 100 PESOS
- Tiempo de servicio: de 5 a 10 años Aumento: 250 PESOS
- Tiempo de servicio: de 10 a 20 años Aumento: 400 PESOS.
- Tiempo de servicio: de 20 años a más Aumento: 550 PESOS.

'''

def salario():
    
    for i in range(4):
        #input
        salario=int(input("Ingrese su salirio: "))
        tiempo=int(input("Ingrese numero de años trabajados en la empresa: "))
        #Tiempo de servicio: de 1 a 5 
        if tiempo >0 and tiempo <5:
            junior = salario * 100
            print("Nuevo salario es: {}".format(junior))

        #Tiempo de servicio: de 5 a 10 años
        elif tiempo >=5 and tiempo <10:
            semiSenior= salario + 250
            print("Nuevo salario es: {}".format(semiSenior))

        #Tiempo de servicio: de 10 a 20 años
        elif tiempo >=10 and tiempo <20:
            senior= salario + 400
            print("Nuevo salario es: {}".format(senior))

        #Tiempo de servicio: de 20 años a más
        elif tiempo >= 20:
            jefe= salario + 550
            print("Nuevo salario es: {}".format(jefe))



salario()