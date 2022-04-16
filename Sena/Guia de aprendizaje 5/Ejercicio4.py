'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó $10, el segundo $20,
el tercero $40 y así sucesivamente. Realice un algoritmo para determinar cuánto debe pagar
mensualmente y el total de lo que pagó después de los 20 meses y represéntelo mediante
pseudocódigo y el utilizando el ciclo apropiado.

'''

def deuda():
    mes=0
    suma=0
    for i in range(1,21):
        if i== 1:
           mes=10
        else:
            mes = mes * 2
            suma= suma + mes
        print("pago del mes {} es: {}".format(i,mes))
        
    print("Total a pagar en los 20 meses es: {}".format(suma))
         
deuda()
