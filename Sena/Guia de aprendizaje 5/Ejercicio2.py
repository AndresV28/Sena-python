'''
Generar la serie: 1, 5, 3, 7, 5, 9, 7, ..., 23

'''

def serie():
    for i in range(1,21):
        #conditional
        if i % 2== 0: # si es numero par , lo comprobamos con el residuo
            print(i+3, end=" ")
        else:         # si es numero impar, no hay necesidad de mirar el residuo
            print(i, end=" ")
        
serie()
