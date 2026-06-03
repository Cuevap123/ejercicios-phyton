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
