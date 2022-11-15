''' Ejercico 14
Escribir un programa que pregunte el nombre completo del usuario 
en la consola y después muestre por pantalla el nombre completo 
del usuario tres veces, una con todas las letras minúsculas, otra
con todas las letras mayúsculas y otra solo con la primera letra
del nombre y de los apellidos en mayúscula. El usuario puede 
ntroducir su nombre combinando mayúsculas y minúsculas como quiera.'''

# Pregunrta al usuario su nombre
nombre = input("¿Cómo te llamas? ")

print(nombre.lower()) # Imprime todo en minusculas
print(nombre.upper()) # Imprime todo en mayusculas
print(nombre.title()) # Imprime todo con la primera letra en mayusculas