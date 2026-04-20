nombre, apellido  = "Andrea", "Cueva"
nombre_completo = nombre+" "+apellido
print (nombre_completo)
print ("I think I'm too cool to know ya\n You say I'm like the ice, I freeze \n I'm churning out novels like \n Beat poetry on amphetamines")
#Desempaquetar nombre
nombre = "Andrea"
a,b,c,d,e,f = nombre
print (a,b,c,d,e,f)
first_letter = nombre[0]
print(first_letter) 
print (nombre[3:6])
print (nombre[::-1])
    #DEBER 4
texto = "Programación Para Todos"
print(texto)
print(len(texto))
print(texto.upper())       
print(texto.lower())       
print(texto.title())      
print(texto.capitalize())  
print(texto.startswith("Programación"))  
print(texto.endswith("Todos"))          
print(texto.find("Para"))               
print("Python" in texto)                 
nuevo_texto = texto.replace("Programación", "Python")
print(nuevo_texto)
palabras = texto.split()
print(palabras)
union = " - ".join(palabras)
print(union)
print(texto[0])    
print(texto[-1])   
print(texto[5])    
nombre = "Andrea Cueva"
print(f"Hola, mi nombre es {nombre}")
iniciales = "".join([palabra[0] for palabra in nombre.split()])
print(iniciales)
