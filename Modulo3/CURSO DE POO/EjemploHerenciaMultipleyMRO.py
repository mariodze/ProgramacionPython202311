# ANIMAL    metodo comer
# MAMIFERO  metodo amamantar
# AVE       metodo volar








class Animal:
    def comer(self):
        print('Comiendo....')



class Mamifero(Animal):
    def amamantar(self):
        print('Amamantando....')


class Ave(Animal):
    def volar(self):
        print('volando....')


class Murcielago(Mamifero,Ave):
    pass


ave = Murcielago()
ave.comer()
ave.amamantar()
ave.comer()


print(Murcielago.mro())