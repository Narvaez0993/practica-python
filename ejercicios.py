#PUNTO 1 - Imprimir el factorial de cualquier numero

"""factorial = input ('ingresa un numero ')

factorial = int (factorial)

def calculafactorial(factorial):

    if factorial==0 or factorial==1:
            resultado=1
    elif factorial > 1:
            resultado=factorial*calculafactorial(factorial-1)
    return resultado


print("el factorial de",factorial ,"es: ",calculafactorial(factorial))"""



# punto 2 - Mostrar los N primeros números de la serie Fibonacci

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



# punto 3 - Retornar el valor de la cuota de un prestamo, teniendo en cuenta que se debe especificar el valor del préstamo, número de cuotas, tasa mensual

"""VlorPrestamo = int(input("Ingrese la cantidad de dinero que requiere: "))

NumeroCuotas = int(input("Ingrese el numero de cuotas a pagar:  "))

def calcularCuota(VlorPrestamo,NumeroCuotas):

  cantidadPago = VlorPrestamo / NumeroCuotas

  TasaInteres = cantidadPago * 0.03

  total = cantidadPago + TasaInteres

  total = int(total)

  return total

print("El valor total de la cuota mensual es: ",calcularCuota(VlorPrestamo,NumeroCuotas))"""


#punto 4 - Mostrar los datos de cualquier array

"""numero = ["hola","arreglo","array"]
print(numero)"""


#punto 5 -  Mostrar los datos de cualquier diccionario

"""diccionario = {
  "nombre": "sebastian",
  "apellido": "mejia",
  "telefono": "3197060463"
}

print(diccionario)"""


#punto 6 . Retornar el total de los pagos del diccionario dpagos= {"placa":"tis123","marca":"Aveo","pagos":[100,200,30,400], enviado como parámetro


# punto pendiente, no se entiende del todo!

"""def imprimirPagos():

  dpagos= {
    "placa":"tis123",
    "marca":"Aveo",
    "pagos":[100,200,30,400]
  }

  return dpagos.get("pagos");

print (sum(imprimirPagos()));"""


# punto 7 Crear un diccionario con variables

"""nombre = input("ingrese su nombre ");
apellido = input("ingrese su apellido ");
edad = input("ingrese su edad ");

diccionario = {
    "Nombre": nombre,
    "Ciudad": apellido,
    "Edad": edad,
}

print(diccionario)"""



# punto 8  Crear una lista con los números del 1 al 50

# punto 9 - Crear una lista con los números impares de la lista generada en el numeral 3.

"""dato = int(input("Ingrese la cantidad de numeros que quiere imprimir:  "))
lista = []
impares = []
count = 0
numero = 0
while count < dato:
  numero = numero + 1
  if numero%2 != 0:
    impares.append(numero)
  count = count + 1
  lista.append(numero)


print(lista)
print(impares)"""


# 10 - Crear un diccionario con los datos de un vehiculo (placa, marca, modelo,valor)

"""placa = input("ingrese la placa del vehiculo ")
marca = input("ingrese la marca del vehiculo ")
modelo = input("ingrese el modelo del vehiculo ")
valor = input("ingrese el costo del vehiculo ")


def RegistrarVehiculo(placa,marca,modelo,valor):
  
  Vehiculo = {
      "placa": placa,
      "marca": marca,
      "modelo": modelo,
      "valor": valor
    }


  return Vehiculo


print(RegistrarVehiculo(placa,marca,modelo,valor))"""


#11 Listar los datos del diccionario generado en el numeral 5 - pendiente



#12 Crear una lista, con datos por teclado, que contenga las ciudades turísticas de Colombia

"""ciudades = []

cantCiudades = input("ingrese la cantidad de ciudades que desea registrar: ")
cantCiudades = int(cantCiudades)

for x in range(cantCiudades):

  Ciudad = input("Ingrese Ciudades turisticas de colombia: ")
  ciudades.append(Ciudad)

print(ciudades)

#13 Agregar una ciudad turística a la lista de ciudades turísticas
añardirCiudad = input("ingrese la ciudad a agregar: ")
ciudades.append(añardirCiudad)

print(ciudades)

#14 Ingresar el nombre de una ciudad y borrarla de la lista ciudades turísticas

eliminarCiudad = input("Ingrese la ciudad que quiere eliminar: ")

if(eliminarCiudad in ciudades):  
  print("Ciudad eliminada correctamente: ")
  ciudades.remove(eliminarCiudad)
  print (ciudades)
else:
  print("La ciudad ingresada no existe, intentalo nuevamente")"""


#15  Crear una clase con los datos de un vehículo (placa, marca, modelo, precio). Los atributos son privados

"""class vehiculo():
    def __init__(self, placa, marca, modelo, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def __repr__(self):
       return f"Placa: {self.placa}\nMarca: {self.marca}\nModelo: {self.modelo}\nPrecio: {self.precio}"
vehiculo1 = vehiculo('ews396', 'Tesla', '2021', '2000000')
print(vehiculo1)"""



































