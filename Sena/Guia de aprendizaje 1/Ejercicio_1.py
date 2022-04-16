'''
1) Escribir un programa que sume, reste, multiplique y divida dos números
'''

def Calculadora():
    # MENU
    print("------ Calculadora ------ ");
    print("-------------------------------------------")
    print("----- Menu -----");
    print("[1] Suma");
    print("[2] Resta");
    print("[3] Multiplicacion");
    print("[4] Division");
    
    # Input del menu con try para fallo de error humano
    while True:
        try:
            opcion=int(input("Ingrese una opcion del menu: "));
            break

        except:
            print("Por favor ingrese un numero");

    #Input de variables 

    num1= int(input("Ingrese el primer numero: "));
    num2=int(input("Ingrese el segundo numero: "));

    #Condicionales para la calculadora  e imprimir resultados

    if opcion ==1 :
        suma = (num1 + num2);
        print("El resultado de la suma de los numeros {} y {} es: {}".format(num1,num2,suma));

    elif opcion== 2:
        resta= (num1 - num2);
        print("El resultado de la resta de los numeros {} y {} es: {}".format(num1,num2,resta));

    elif opcion == 3:
         multiplicacion= (num1 * num2);
         print("El resultado de la multiplicacion de los numeros {} y {} es: {}".format(num1,num2,multiplicacion));
    
    elif opcion == 4:
        division= (num1 / num2);
        print("El resultado de la division de los numeros {} y {} es: {}".format(num1,num2,division));

Calculadora()