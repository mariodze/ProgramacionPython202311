
#Herencia multiple : si una clase tiene atributos y metodos de otras clases



#CLASE PADRE 1
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('Hola, estoy hablando un poco')

#CLASE PADRE 2

class Artista:
    def __init__(self,habilidad):
        self.habilidad= habilidad

    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'
    

#Clase hijo o subclase:

class EmpleadoArtista(Persona, Artista):          
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario): 
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print (f'Hola mi nombre es {self.nombre}. {self.mostrar_habilidad()} y trabajo en {self.empresa}')




roberto = EmpleadoArtista('Roberto',43, 'peruano','Cantar', 'google',1000000)

roberto.presentarse()




#### PARA SABER AHORA SI UNA CLASE ES HIJA DE OTRA 
herencia =issubclass ( EmpleadoArtista, Persona)
                        #clase hija      #clase padre
print(herencia)  #da resultados de True o False


instancia = isinstance (roberto,           Artista)
                        #instancia//objeto   #clase
print(instancia)  #da resultados de True o False