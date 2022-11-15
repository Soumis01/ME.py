''' Ejercico 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada 
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada 
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa 
que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso
 total del paquete que será enviado.'''

# Definimos valores
payasos = 112 
munecas = 75 

# Preguntamos al usuario
total_payasos = int(input('Cual es el numero de payasos a enviar?: '))
total_munecas = int(input('Cual es el numero de muñecas a enviar?: '))

# Hacemos la multiplicacion y suma de todo 
total_enviar = payasos * total_payasos + munecas * total_munecas

print('El total del envio es: ' + str(total_enviar))