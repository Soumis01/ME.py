''' Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés 
al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te 
añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo
 la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
 Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras 
 el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.'''

saldo = float(input('Ingresa la cantidad a ahorrar: '))

for x in range(3): # Utilizamos el ciclo for y generamos un rango (range) este seran nuestros 3 años
    interes = saldo * .04 # Multiplicamos el saldo por el interes
    saldo = saldo + interes # y sumamos el sado con el resusltado del interes
    
    print('Tu saldo en el año: ' , x+1, ': es $', round(saldo,1))