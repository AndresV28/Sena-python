'''
Diseñar un pseudocódigo que calcule el promedio ponderado para alumno del ITT. El cálculo se hace
de la siguiente forma: Se multiplica cada calificación por los créditos de cada materia
El resultado anterior se suma con los resultados de todas las materias, por separado se suman los
créditos de cada materia y finalmente se divide la suma de todas las materias por sus respectivos
créditos, entre la suma de todos los créditos. (materias: Fundamentos, BD y ética).
'''
#variables de creditos entran por valor  y notas tambien por valor
def promedio(funda,base,etic,fundamentos,bd,etica):
    #--------------- NOTAS ---------------

    nota1= funda* fundamentos  #fundamentos 
    nota2= base * bd   #base de datos
    nota3= etic * etica # etica

    #suma de todas las materias
    totalNotas= nota1+nota2+nota3
  
    return totalNotas # retornamos suma de las notas

#variables creditos
fundamentos= 4
bd= 3
etica=2

#pedimos notas
funda=float(input("Ingrese calificacion de fundamentos: "))
base=float(input("Ingrese calificacion de BD: "))
etic=float(input("Ingrese calificacion de etica: "))
promedio(funda,base,etic,fundamentos,bd,etica) # llamado de la funcion

#------------ despues del retorno de la funcion -----------------
notasFinal= promedio(funda,base,etic,fundamentos,bd,etica) # retornamos valor a la variable notas final
sumaCreditos= fundamentos + bd + etica #suma creditos

#promedio
promedioFinal= notasFinal / sumaCreditos
print("El promedio de las notas es: {}".format(round(promedioFinal,2))) #print del resultado