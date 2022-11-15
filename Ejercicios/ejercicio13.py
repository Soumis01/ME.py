''' Ejercicio 13
Escribir un programa que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla en líneas distintas el 
nombre del usuario tantas veces como el número introducido.'''

# Preguntamos al usuario los datos
nombre = input('Cual es tu nombre?: ')
n = int(input('Escribe un numero entero: '))

# Imprimimos el nombre, hacemos salto de linea y multiplicamos n por el numero introducido
print ((nombre + '\r\n') * n)