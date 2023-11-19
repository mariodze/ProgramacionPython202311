# Las funciones son aquellas que a partir de un conjunto de valores de entrada (inputs) van a arrojar una salida
# EN programación, una funcion será un segmento de código que ayuda a dividir mi programa en procesos más sencillos

# todo numero es primo

def evaluar_primo(numero):
    
    if numero==1:
        return False
    
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            # encontre un divisor
            es_primo = False
            break
    return es_primo


# Ejemplo, realizar un programa que muestre los número primos del 1 al 100

listado_primos = []
for numero in range(1,101):
    # evaluar que número son primos
    if evaluar_primo(numero):
        listado_primos.append(numero)
    

print('Imprimiendo el listado de número primos entre el 1 y el 100')
print(listado_primos)









