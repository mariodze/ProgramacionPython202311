# Herencia simple:  padre e hijo ---- suplerclase y subclase


# Clase padre o superclase: 

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad
    def hablar(self):
        print('Hola, estoy hablando un poco')

#Clase hijo o subclase:

class Empleado(Persona):          #Aqui ponemos que va a heredar atributos y/o  metodos dela clase persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): # trabajo y salario son nuevos atributos y exclusivo de la clase empleado
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario



roberto = Empleado('Roberto',43, 'peruano','programacion',1000000)

roberto.hablar()