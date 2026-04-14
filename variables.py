"""Andrea Cueva 
10/4/2026
Variables"""
#Ejercicico nivel 1
nombre,apellido,nombre_completo,pais,ciudad,año,esta_casado,es_verdadero,luz_encendida, edad = "Andrea", "Cueva", "Andrea Cueva", "Ecuador", "Quito",2026, False,  True, "encendida", 16
print (type(nombre))
print (type(apellido))
print (type(nombre_completo))
print (type(pais))
print (type(ciudad))
print (type(año))
print (type(edad))
print (type(esta_casado))
print (type(es_verdadero))
print (type(luz_encendida))
print (len(nombre))
print(len(nombre) > len(apellido))
n1, n2 = 5, 4
total = n1 + n2
diferencia = n1 - n2
producto = n1 * n2
division = n1 / n2
residuo = n2 % n1
potencia = n1 ** n2
divisionEntera = n1 // n2
radio, pi = 30, 3.1416
areaCirculo = pi * radio ** 2
circunferenciaCirculo = 2 * pi * radio
print(areaCirculo)
print(circunferenciaCirculo)
radio = float(input("Ingresa el radio: "))
area = pi * radio ** 2
print("Área:", area)
nombre = input("Nombre: ")
apellido = input("Apellido: ")
pais = input("País: ")
edad = int(input("Edad: "))
help('keywords')
#DEBER
#ejercicio 1
edad = 16
#ejercio 2
estatura = 1.60
#ejercicio 3
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = 0.5 * base * altura 
print ("El area de tu triangulo es: ",area)
#ejercicio 4
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))
perimetro = a + b + c
print ("El perimetro de tu triangulo es: ",perimetro)
#ejercicio 5
longitud = float(input("Ingrese la longitud: "))
ancho = float(input("Ingrese el ancho: "))
area = longitud * ancho
perimetro = 2 * (longitud + ancho)
print("Área:", area)
print("Perímetro:", perimetro)
#ejercicio 6
radio = float(input("Ingrese el radio: "))
pi = 3.14
area = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área:", area)
print("Circunferencia:", circunferencia)
#ejercicio 7
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La pendiente es:", m)
print("La distancia es:", distancia)
#ejercicio 7
x = int(input("Ingrese un valor de x: "))
y = x**2 + 6*x + 9
print("y =", y)
x = -3
a = len("python")
b = len("dragon")
print(a == b)
print("on" in "python" and "on" in "dragon")
oracion = "Espero que este curso no esté lleno de jerga."
print("jerga" in oracion)
print("on" in "python" and "on" in "dragon")
longitud = len("python")
a = float(longitud)
b = str(a)
print(b)
print(7 // 3 == int(2.7))
print(type("10") == type(10))
print(int(float('9.8')) == 10)
horas = float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))
pago = horas * tarifa
print("Pago total:", pago)
años = int(input("Años vividos: "))
segundos = años * 365 * 24 * 60 * 60
print("Segundos vividos:", segundos)
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

