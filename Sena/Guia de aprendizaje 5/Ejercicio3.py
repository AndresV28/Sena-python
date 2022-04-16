''''
La Universidad del Valle requiere un programa que le permita conocer cómo califican los estudiantes
la comida de la cafetería central. Para ello definió una escala de 1 a 10 (1 denota horrible y 10 denota
excelente). El programa debe ser capaz capturar la calificación de cualquier número de estudiantes
(no se sabe cuántos estudiantes se encuestarán, así que cuando el encuestador ingrese la calificación
de 0, se sabrá que la encuesta habrá concluido). El programa deberá mostrar en su salida cuántos
estudiantes fueron encuestados, así como el resumen de la encuesta como el promedio y cuál es la
nota más alta dada y la nota más baja dada en la encuesta efectuada.
'''

def universidad():
    lista=[]
    #variables
    mayor=0
    menor=0
    suma=0 # variable suma
    contador=0 #Contador de encuentados
    #ciclo for
    for i in range(5000): # POR MEJORAR ESTO
  
        calificacion=int(input("Ingrese su calificacion: ")) #input  de calificaciones
    
        #Conditional
        if calificacion > 0 and calificacion <=10:
            lista.append(calificacion) #agregramos la calificacion a una lista
            suma= suma + calificacion # suma de promedio
            contador = contador + 1 #contadro de encuentados
        elif calificacion == 0:
            print("Encuesta terminada")
            break  #Rompemos ciclo 
      
    #numero mayor y numero menor
    '''
    for z in range(len(lista)):
        print(lista[z], end=" ")
    '''
    c = lista[0]
    d= lista[0]
    for y in range(len(lista)):  # for para recorrer la lista 
        if c < lista[y]:
            c= lista[y]
            mayor= c    #numero mayor

        if d > lista[y]: 
            d=lista[y]
            menor = lista[y]  # numero menor

    total= suma / contador # hacemos promedio de encuestados
    #Print
    print("Total de estudiantes encuentados fue: {}".format(contador))
    print("Promedio de calificacion de la cafeteria es: {}".format(round(total,2)))
    print("Numero mayor: {}".format(mayor))
    print("Numero menor: {}".format(menor))

universidad()