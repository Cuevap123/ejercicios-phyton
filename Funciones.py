def obtener_mensaje(mensaje):
    return mensaje
def generar_nombre_completo(nombre,apellido):
    nombre_completo = nombre + " " + apellido
    return nombre_completo
mensaje = str(input("Ingrese el mensaje: "))
nombre = str(input("Ingrese el nombre: "))
apellido = str(input("Ingrese el apellido: "))
print(f"{obtener_mensaje(mensaje)}, {generar_nombre_completo(nombre,apellido)}")


def operacion1(n1,n2):
    resultado = n1 + n2
    return resultado

def operacion2():
    return n1 * n2

def operacion3():
    return n1 - n2

def operacion4():
    return n1 / n2

print("1. Suma")
print("2. Multiplicación")
print("3. Resta")
print("4. División")
print("5. Salir")

n1 = int(input("Ingrese el primer numero :"))
n2 = int(input("Ingrese el segundo  numero :"))
while True:
    op = int(input("Ingrese qué operación va a realizar: "))
    if op == 1:
        print(f"el resultado es : { operacion1(n1,n2)}")
    elif op ==2 :
        print(f"el resultado es : { operacion2(n1,n2)}")
    elif op == 3:
        print(f"el resultado es : { operacion3(n1,n2)}")
    elif op ==4:
        print(f"el resultado es : { operacion1(n1,n2)}")
    elif op == 5:
        print ("Programa finalizado")
        break
    else:
        print("Opcion no valida")

#Deber:
def calcular_promedio(n1, n2, n3):

    promedio = (n1 + n2 + n3) / 3

    return promedio
 
 
def nota_mayor(n1, n2, n3):

    mayor = max(n1, n2, n3)

    return mayor
 
 
def nota_menor(n1, n2, n3):

    menor = min(n1, n2, n3)

    return menor
 
 
def determinar_aprobacion(promedio):

    if promedio >= 60:   

        return "El estudiante aprueba"

    else:

        return "El estudiante repueba"
 
 
print("=== MENÚ DE CALIFICACIONES ===")
 
n1 = float(input("Ingrese la primera calificación: "))

n2 = float(input("Ingrese la segunda calificación: "))

n3 = float(input("Ingrese la tercera calificación: "))
 
while True:

    print("\nMenú:")

    print("1. Calcular el promedio")

    print("2. Mostrar la nota mayor")

    print("3. Mostrar la nota menor")

    print("4. Determinar si aprueba o reprueba")

    print("5. Salir")
 
    opcion = input("Seleccione una opción: ")
 
    if opcion == "1":

        resultado = calcular_promedio(n1, n2, n3)

        print("Promedio:", resultado)
 
    elif opcion == "2":

        resultado = nota_mayor(n1, n2, n3)

        print("Nota mayor:", resultado)
 
    elif opcion == "3":

        resultado = nota_menor(n1, n2, n3)

        print("Nota menor:", resultado)
 
    elif opcion == "4":

        promedio = calcular_promedio(n1, n2, n3)

        resultado = determinar_aprobacion(promedio)

        print(resultado)
 
    elif opcion == "5":

        print("Saliendo del programa...")

        break
 
    else:

        print("Opción no válida. Intente nuevamente.")
 
