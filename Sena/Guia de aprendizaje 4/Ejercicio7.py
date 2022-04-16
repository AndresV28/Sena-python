'''
Cinco miembros de un club contra la obesidad desean saber cuánto han bajado o subido de peso
desde la última vez que se reunieron. Para esto se debe realizar un ritual de pesaje en donde cada
uno se pesa en diez básculas distintas para así tener el promedio más exacto de su peso. Si existe
diferencia positiva entre este promedio de peso y el peso de la última vez que se reunieron, significa
que subieron de peso. Pero si la diferencia es negativa, significa que bajaron. Lo que el problema
requiere es que por cada persona se imprima un letrero que diga: “SUBIO” o “BAJO” y la cantidad de
kilos que subió o bajo de peso.

'''

def pesos():

    #variable
    x=0 #contador para ver miembros
    y=0 # iniciar ciclo interno
    z= 0 # romper whilw true
    n=0 # numero de basculas
    peso=0 #pormedio de pesos
    basculas=3


    miembros=int(input("Ingrese cantidad de mienbros: "))

    for i in range(miembros): 
        
        print("Miembro # {}".format(x+1))
        pesoAnterior=float(input("Ingrese su peso anterior: "))
        x=x+1

        while (True):

            Bascula= float(input("Sube a la bascula numero {}: ".format((y+1))))
            peso= peso + Bascula  #peso total por todas las basculas
            y=y+1 # contador para mostrar que miembro sigue

            n=n+1 #contador de vueltas de baculas para entrar al if
            totalPeso = peso / basculas #promedio de peso segun numero de basculas

            if n == basculas: #rompemos ciclo interno para que ingrese el for
                break

        #reseteo de variables
        y= 0
        n=0
        peso=0

        #PRINT
        print("------------------------------------------")
        if pesoAnterior > totalPeso:
            bajo= pesoAnterior - totalPeso
            print("Haz bajado un total de: {} kg".format(bajo))
            print("------------------------------------------")

        elif totalPeso > pesoAnterior:
            subio = pesoAnterior - totalPeso
            total= subio * -1
            print("Haz subido un total de: {} kg".format(total))
            print("------------------------------------------")
        
pesos()        

        

        
   

        
