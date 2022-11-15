''' Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en la inversión. '''

def hallar_inversion(): # Funcion para agregar los datos a llenar
    cantidad_invertir = int(input('Ingrese la cantidad a invertir: '))
    interes_anual = int(input('ingrse el interes anual: '))
    numeros_años = int(input('Ingrese el numro de años: '))

# Multiplica los datos dados por el usuario
    interes_total  = interes_anual * numeros_años
    canidad_total = interes_total * cantidad_invertir

    print('capital_incvertido')

hallar_inversion()




