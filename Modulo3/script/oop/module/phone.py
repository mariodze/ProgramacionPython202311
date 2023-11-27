import uuid

class Contacto:
    name=""
    phone=""
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def __str__(self):
        return f"{self.name}-{self.phone}"
    pass
class Agenda:
    pass


class Perfil:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
    def __str__(self):
        return f"{self.name} con email {self.email}"

class Phone:
    def __init__(self,marca,modelo,memoria_ram,memoria_sd,duracion_bateria):
        self.number_assign=""
        self.perfil:Perfil=""
        self.switch_power=False
        self.estado="ACTIVO"
        self.serie=uuid.uuid4()
        self.marca=marca
        self.modelo=modelo
        self.memoria_ram=memoria_ram
        self.memoria_sd=memoria_sd
        self.duracion_bateria=duracion_bateria
        self.pin="123"
        self.Agenda=[]
    
    def showPower(self):
        if self.switch_power:
            print("el equipo esta prendido")
        else:
            print("el equipo esta apagado")

    def toggle_power(self):
        self.switch_power=not self.switch_power
    def config_profile(self):
        name=input("ingrese el name ")
        email=input("ingrese el email ")
        password=input("ingrese el password ")
        p1=Perfil(name,email,password)
        self.perfil=p1
    def shwo_config(self):
        print(self.perfil)
        
    def setPin(self,pin):
        self.pin=pin
    def validPin(self)->bool:
        if len(self.pin)!=0:
            pinTmp=input("ingrese su pin")
            if self.pin==pinTmp:
                return True
            else:
                return False
        else:
            while True:
                print("configure su pin")
                pinTmp2=input("ingrese su pin nuevo")
                pinTmp3=input("verifique su pin ")
                if(pinTmp3==pinTmp2):
                    self.setPin(pinTmp2)
                    break
                else:
                    print("ingrese 2 pin validos")
            return False
    
    def agregarContacto(self):
        name=input("ingrese el name ")
        phone=input("ingrese el phone")
        c1=Contacto(name,phone)
        if self.validPin():
            self.Agenda.append(c1)
        else:
            print("no tiene acceso a la agenda")
    def showAgenda(self):
        if len(self.Agenda)>0:
            for i in self.Agenda:
                print(i)

