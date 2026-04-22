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
edad = int(input("Ingrese la edad:"))
print("Es mayor de edad") if edad > 18 else print("Es menor de edad")
