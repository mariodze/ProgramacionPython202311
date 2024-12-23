# EJERCICIO 1: (HERENCIA SIMPLE)

# Crear un sistema para una escuelA. En este sistema, vamos a tener dos clases principales
# PERSONA : nombre y edad , metodo que imprima nombre y edad de la persona
# ESTUDIANTE heredara de la clase PERSONA , atributo adicional: grado y metodo 
# que imprima el grado delestudiante


class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_persona(self):
        return (f'{self.nombre} tiene {self.edad} años')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def grado_estudiante(self):
        return (f'El grado del estudiante es de {self.grado}')



Mario = Estudiante('Mario',24,'5to ciclo')
print(f'{Mario.mostrar_persona()}. {Mario.grado_estudiante()}')