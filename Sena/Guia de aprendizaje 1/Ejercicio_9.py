'''
9)Programa que muestre el pago de una llamada telefónica sabiendo que cada minuto cuesta $355
pesos y un IVA de 20%.
'''

def llamada():
    # INPUT
    minuto=int(input("Ingrese cantidad de minutos consumidos: "));

    #OPERACIONES MATEMATICAS 

    valorMin= minuto * 355; # valor de los minutos
    iva= valorMin * 0.2; # iva de los minutos
    resultado = valorMin + iva; # valor total de los minutos 

    #PRINT RESULTADO

    print("Total de los minutos es: {}".format(resultado));

llamada()
