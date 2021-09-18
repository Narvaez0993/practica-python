from _typeshed import Self


class Animal:
    peso = 0.0
    def __init__(self,peso):
        self.peso = peso

    def Comer(self):
        print("Comiendo")

class Oviparo(Animal):
    def ponerHuevos(self):
        print("poniendo huevos")

class mamifero(Animal):
    sangreCaliente = True

    def __init__(self,sangreCaliente):
        self.sangreCaliente = sangreCaliente
    
    def Parir(self):
        print("pariendo")
    
    def Amamantar(self):
        print("amamantando")

class delfin(mamifero):
    def nadar():
        print("nadando")

class perro(mamifero):
    colorPelo = ""
    
    def __init__(self,colorPelo):
        self.colorPelo = colorPelo

    def ladrar(self):
        print("woof woof ...")

    

    