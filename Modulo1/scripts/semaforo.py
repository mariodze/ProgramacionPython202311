"""
Crear un programa que permita decidir a una persona cruzar la calle o no según:
- Si semáforo esta en verde cruzar la calle
- Si semáforo esta en rojo o amarillo no cruzar

La persona debe poder ingresar el estado del semáforo por teclado
"""

# 1. Ingresar el estado del semaforo
# 2. Si semaforo esta en verde, imprimir "puedes cruzar"
# 3. Si semaforo esta en rojo o amarillo, imprimir "no cruzar"

semaforo = input('Ingrese el estado del semaforo: ')

if semaforo == 'verde':
    print('Puedes cruzar')
elif semaforo == 'rojo' or semaforo == 'amarillo':
    print('No cruzar')
else: # para cualquier otra casuhistica
    print('Comando no reconocido')


