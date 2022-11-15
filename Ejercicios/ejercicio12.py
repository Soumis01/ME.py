''' Ejercico 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es
el día tiene un descuento del 60%. Escribir un programa que comience
leyendo el número de barras vendidas que no son del día. Después 
el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.'''

# Preguntamos al usuario para que introduzca un entero
barras = int(input('Por favor introduza las barras vendidas que no son del dia: '))

print('Precio habitual es: 3.49');

# Hacemos el calculo para saber cual es el 60% del precio
descuento = float((3.49 / 100) * 60);
print('Descuento por barra seria de: ' + str(descuento))

# Para el precio final tomamos el precio y restamos el descuento
precio_final = float(3.49 - descuento);

# El total es el numero de barras por el precio final
total = barras * precio_final;

print('Precio final: ' + str(total));

