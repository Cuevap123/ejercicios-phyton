"""n = int(input("Ingrese un numero:" ))
if n  > 0 and n % 2 == 0:
    print("El numero es positivo y par")
elif n > 0: 
    print("El numero es positivo e impar")
elif n < 0  and n % 2 == 0:
    print("El numero es negativo e par")
elif n<0: 
    print ("El numero es negativo impar")
else: 
    print ("El numero es 0")"""
#CONDICIONALES ANIDADOS
"""n = int(input("Ingrese un numero:"))
if n  == 0:
    print("El numero es 0")
else:
    if n > 0 : 
        if n % 2 == 0:
            print("El numero es positivo e par")
        else:
            print("El numero es positivo e impar")
    else:
        if n % 2 == 0:
            print("El numero es negativo e par")
        else:
            print("El numero es negativo e impar")"""      
#OTRO METODO MAS FACIL 
"""edad = int(input("Ingrese la edad:"))
print("Es mayor de edad") if edad > 18 else print("Es menor de edad")"""

#Deber 5
# Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    faltan = 18 - edad
    print("Necesitas", faltan, "años más para aprender a conducir.")
# Ejercicio 2

mi_edad = int(input("Ingrese mi edad: "))
tu_edad = int(input("Ingrese tu edad: "))

if mi_edad > tu_edad:
    diferencia = mi_edad - tu_edad
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print("Soy", diferencia, "años mayor que tú.")
elif tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print("Eres", diferencia, "años mayor que yo.")
else:
    print("Tenemos la misma edad.")

# Ejercicio 3

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    print(a, "es mayor que", b)
elif a < b:
    print(a, "es menor que", b)
else:
    print(a, "es igual a", b)
# Ejercicio 4

nota = int(input("Ingrese su puntaje: "))

if nota >= 60:
    if nota >= 70:
        if nota >= 80:
            if nota >= 90:
                print("A")
            else:
                print("B")
        else:
            print("C")
    else:
        print("D")
else:
    print("F")

# Ejercicio 5
mes = input("Ingrese el mes: ").lower()

if mes in ["septiembre", "octubre", "noviembre"]:
    print("Otoño")
else:
    if mes in ["diciembre", "enero", "febrero"]:
        print("Invierno")
    else:
        if mes in ["marzo", "abril", "mayo"]:
            print("Primavera")
        else:
            if mes in ["junio", "julio", "agosto"]:
                print("Verano")
            else:
                print("Mes inválido")
# Ejercicio 6
fruits = ['banana', 'orange', 'mango', 'lemon']

fruta = input("Ingrese una fruta: ").lower()

if fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruta)
    print("Lista actualizada:", fruits)
