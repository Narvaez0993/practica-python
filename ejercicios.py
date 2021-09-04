#PUNTO 1

"""factorial = input ('ingresa un numero ')

factorial = int (factorial)

def calculafactorial(factorial):

    if factorial==0 or factorial==1:
            resultado=1
    elif factorial > 1:
            resultado=factorial*calculafactorial(factorial-1)
    return resultado


print("el factorial de",factorial ,"es: ",calculafactorial(factorial))"""



# punto 2 

"""num = input('ingresa un numero ')

num = int(num)

def calcularFibonacci(num):
    i = 0
    n1 = 0
    n2 = 1
    for i in range(num):
       print(num, end=' ')
       num = (num-1) + (num-2)
    return num

print(calcularFibonacci(num)) """



"""num = input("ingrese el numero limite del fibonacci a imprimir: ")
num = int(num)
def calcularFibonacci(num):
#ingresar un numero correcto
  n1= 0 
  n2 =  1
  count = 1
  if num <= 0:
    print("Opss ingresaste un numero incorrecto, revisa y intentalo nuevamente")
  else:
    print("secuencia fibonacci: ")
    while count < num:
        print(n1)
        resultado = n1 + n2
        n1 = n2
        n2 = resultado
        count = count + 1
  return n1

print(calcularFibonacci(num))"""



# punto 3 

"""VlorPrestamo = int(input("Ingrese la cantidad de dinero que requiere: "))

NumeroCuotas = int(input("Ingrese el numero de cuotas a pagar:  "))

def calcularCuota(VlorPrestamo,NumeroCuotas):

  cantidadPago = VlorPrestamo / NumeroCuotas

  TasaInteres = cantidadPago * 0.03

  total = cantidadPago + TasaInteres

  total = int(total)

  return total

print("El valor total de la cuota mensual es: ",calcularCuota(VlorPrestamo,NumeroCuotas))"""

#punto 4

"""numero = ["hola","arreglo","array"]

print(numero)"""


#punto 5

"""diccionario = {
  "nombre": "sebastian",
  "apellido": "mejia",
  "telefono": "3197060463"
}

print(diccionario)"""


#punto 6 . Retornar el total de los pagos del diccionario dpagos= {"placa":"tis123","marca":"Aveo","pagos":[100,200,30,400]

"""dpagos= {"placa":"tis123","marca":"Aveo","pagos":[100,200,30,400]}

print(sum(dpagos["pagos"]))"""


# punto 7 Crear un diccionario con variables






# punto 8 Crear una lista con los números del 1 al 50
"""dato = int(input("Ingrese la cantidad de numeros que quiere imprimir:  "))
count = 0
numero = 1
while count < dato:
    print(numero)
    numero = numero + 1
    count = count + 1"""



















