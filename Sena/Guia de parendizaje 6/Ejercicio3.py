'''
Calcular el sueldo que le corresponde al trabajador de una empresa que cobra $14.400.000 anual, el
programa debe realizar los cálculos en función de los siguientes criterios:
a. Si lleva más de 10 años en la empresa se le aplica un aumento del 10%.
b. Si lleva menos de 10 años, pero más que 5 se le aplica un aumento del 7%.
c. Si lleva menos de 5 años, pero más que 3 se le aplica un aumento del 5%.
d. Si lleva menos de 3 años se le aplica un aumento del 3%.
'''
# variable AÑOS entra por valor y  PAGO referencia 
def sueldo(años,pago):
    #conditional
    if años > 10:  #trabajo mas de 10 años en la empresa
        aumento= pago * 0.10   #aumento
        total=  pago + aumento  #nuevo sueldo
   
   
    elif años < 10 and años >5: #trabajo mas de 5 años  y menos de 10 años en la empresa
        aumento= pago * 0.07
        total= pago + aumento
        
    
    elif años <5 and años >3: #trabajo 4 años en el empresa
        aumento = pago * 0.05
        total= pago + aumento
      
    
    elif años <3 :          #menos de tres años en la empresa
        aumento= pago* 0.03
        total= pago + aumento

    return total  #retornamos variable a pago

pago=14400000 # se envia por referencia 
años=int(input("Ingrese numero de años trabajados: ")) #se envia por valor 
sueldo(años,pago) # llamado de la funcion !!!!!

pago= sueldo(años,pago) # se trae valor por return
print("Su nuevo sueldo es: {}".format(pago))  # imprimimos nuevo sueldo 
