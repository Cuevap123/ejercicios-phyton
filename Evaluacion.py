# ===== PARTE A =====
#Analisis de datos y codigo
"""nombre = "Lucía"
edad = 16
promedio = 9.75
cursos = ["Python", "HTML", "CSS"]
print("Nombre:",type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(len(nombre))"""

# Respuesta 1:
#a) Indica el tipo de dato de cada variable
#nombre = str
#edad = int
#promedio = float
#cursos = list
#Respuesta 2:
#b) Escribe qué mostraría el programa en pantalla.
#salida:
#  <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'list'>
#Respuesta 3:
#c) Explica qué hace len(nombre).
#El comando len(nombre), lo que hace es contar el numero de caracteres que tiene una variable de texto, decir muestra la cantidad exacta, en este ejemplo seria 5 caracteres o letras.
#2. Comprensión conceptual 
#a) ¿Qué diferencia hay entre print() e input()?
#El comando print (), se usa para mostrar en la pantalla lo que el usuario establece dentro de este, a diferencia delinput() el cual por el contrario solicita al ususario un dato para guarda en alguna variable establecida.
#b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
# puede dar error, si es que no es el tipo de dato correcto que se solicita, es decir para un calculo se necesita un tipo de dato int, no str.
#c) Explica la diferencia entre /, // y %.
#Son operadores matematicos,/ es division la cual muestra el resultado completo, con decimales y enteros, // por otro lado muestra solo la parte entera y  % encambio muestra el modulo de la division  
#d) Escribe una instrucción que permita comprobar la versión de Python que se está usando.
#
#e) Escribe una instrucción que permita consultar las palabras reservadas de Python.
#
# ===== PARTE B =====
# Código corregido
#ancho = int(input("Ingrese el ancho del terreno: "))
#largo = int (input("Ingrese el largo del terreno: "))
#precio = float(input("Ingrese el precio por metro cuadrado: "))
#area = ancho*largo
#costo = area * precio
#print("Área total: " , area)
#print("Costo estimado: " , costo)
#a) ¿Cuáles eran los errores principales?
#Al momento de pedir al usuario el dato, el programa no tenia definido que tipo de dato tenia que ser, por lo que no se podia realizar el calculo con un tipo de variable que no es int.
#b) ¿Por qué tu corrección sí permite obtener resultados válidos?
#Permite obtener resultados validos, ya que se establacio que todos los datos ingresados deben ser int o float en el caso del precio, lo que permite que los calculos se desarrollen con normalidad, sin dar error.
#4. Construcción breve 
#Escribe un fragmento de código que haga lo siguiente:
# Cree la variable frase con el texto "Tecnología para todos".
#  Muestre la frase en mayúsculas.
# Muestre la cantidad de caracteres de la frase.
#Verifique si la palabra "Python" está dentro de la frase.
# Reemplace "Tecnología" por "Programación".
# Divida la frase en palabras usando split(). 
#Codigo:
"""texto = "Tecnología para todos"
print(texto.upper())
print("La cantidad de caracteres es: ",len(texto))
print ("Python" in texto)
frase = texto.replace("Tecnología", "Programación")
print(frase)
print (texto.split())"""
# ===== PARTE C =====
# Programa integrador2
#5. Desarrolla un programa
#Codigo:
nombre = str(input("Ingrese su nombre: "))
apellido = str(input ("Igrese su apellido: "))
pais = str(input("Ingrese su pais: "))
ancho = int(input("Ingrese el ancho de la pared: "))
largo = int (input("Ingrese el alto de la pared: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho*largo
costo = area * precio
nombre_completo = nombre +" " + apellido
print(f"Nombre completo: {nombre_completo}  Pais: {pais} El area calculada es: {area} El costo total es: {costo}")
print(nombre_completo.upper())
print("la longitud es: ",len(nombre_completo))
print ("a" in nombre_completo)
print (costo > 100)
print 