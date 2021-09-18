
class operaciones:
    numero1 = 0
    numero2 = 0
    operacione = ""
    resultado = 0
   
   

    def __init__(self, numero1, numero2, operacione):

        self.numero1 = numero1
        self.numero2 = numero2
        self.operacione = operacione
    
    def imprimir(self):
        print(self.numero1,"",self.operacione,"",self.numero2," = ",self.resultado)

class Suma(operaciones):
    suma = 0

    def __init__(self,numero1,numero2):
     
            self.suma = numero1 + numero2
            self.setRes(self.suma)

        

    
numero1 = 2
numero2 = 3

resultado =  operaciones(numero1,numero2)










