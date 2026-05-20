Numero = int(input("Ingrese el numeo a multiplicar: "))
D = int(input("Ingrese el numero hasta donde se va a multiplicar: "))
x= int(input("Ingrese el numero desde donde se comienza a multiplicar: "))
for i in range(x, D+1):
    m = Numero * i
    print(Numero, "x", i, "=", m)
