#Clases, objetos(instancias de clase), atributos y metodos

# crear una clase estudiante
# Atributos  Nombre,edad y grado
# Metodo 
# estudiar() que imrpima el mensaje 'el estudiante (nombre) esta estudiando'

# crear una instancia y usar el metodo estudiar()
# se debe interactuar con el usuario y este debe brindar los atributos

class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'el estudiante {self.nombre} esta estudiando')


print('Hola estudiante')
name = input('Ingrese su nombre: ')
age = input('Ingrese su edad: ')
grade = input('Ingrese su grado: ')
estudiante1 = Estudiante(name,age,grade)

print (f'\n    DATOS DEL ESTUDIANTE    \nNombre: {estudiante1.nombre}\nEdad: {estudiante1.edad}\nGrado: {estudiante1.grado} ')



while True:
    palabra= input('que accion desea realizar: ')
    if palabra.lower() == 'estudiar':
        estudiante1.estudiar()
        break
    