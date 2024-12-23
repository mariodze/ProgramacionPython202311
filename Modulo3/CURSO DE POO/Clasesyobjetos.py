
#Clases, objetos(instancias de clase), atributos y metodos

class Celular:
    def __init__(self, marca, modelo, camara):    #constructor marca, modelo y camara son los parametros
        self.marca = marca        #atributos de instancia no estaticos
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'Estas haciendo un llamado desde un : {self.modelo}')   # metodos
    
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')



celular1= Celular('Samsung','S23','48MP')
celular2= Celular('Apple','Iphone 15 Pro Max','96MP')

celular2.llamar()
