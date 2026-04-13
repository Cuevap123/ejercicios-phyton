"""Andrea Cueva 
10/4/2026
Variables"""
#Ejercicio nivel 1
nombre,apellido,nombre_completo,pais,ciudad,año,esta_casado,es_verdadero,luz_encendida, edad = "Andrea", "Cueva", "Andrea Cueva", "Ecuador", "Quito",2026, False,  True, "encendida", 16
#Ejercicio nivel 2
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
