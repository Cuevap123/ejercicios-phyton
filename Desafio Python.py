nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
puntaje = int(input("Ingrese su puntaje: "))
asistencia = int(input("Ingrese su asistencia; "))
codigo_invitacion =  str(input("Ingrese su nombre: "))
print(nombre.upper())
print (len(nombre))

promedio = (puntaje + asistencia)/2

if edad >= 14:
    if promedio >= 80:
        if codigo_invitacion == "PYTHON2026":
            print("Acceso VIP")
        else:
            print("Acceso general")
    if promedio  >  60 and promedio < 79:
        print("Acceso con observacion")
    if promedio < 60:
        print("No puede ingresar por bajo rendimiendo")
else:
    if edad <14:
        if codigo_invitacion == "PYTHON2026":
            print("Acesso especial con acompañante")
    else:
        print ("No cumple con la edad minima")

if puntaje >= 90 or asistencia >= 90:
    print("Candidato destacado")
elif puntaje <=50 or asistencia <= 50:
    print("Requiere refuerzo previo")


