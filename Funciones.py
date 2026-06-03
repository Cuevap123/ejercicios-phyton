def obtener_mensaje(mensaje):
    return mensaje
def generar_nombre_completo(nombre,apellido):
    nombre_completo = nombre + " " + apellido
    return nombre_completo
mensaje = str(input("Ingrese el mensaje: "))
nombre = str(input("Ingrese el nombre: "))
apellido = str(input("Ingrese el apellido: "))
print(f"{obtener_mensaje(mensaje)}, {generar_nombre_completo(nombre,apellido)}")
