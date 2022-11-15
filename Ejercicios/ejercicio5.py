''' Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''

# Pregunto al usuario los datos
horas = float(input('Introduce las horas que trabajas: '))
coste = float(input('Introduce lo que cobras por hora: '))
paga = horas * coste # Multiplico los datos dados por el usuario

print('Tu paga es', paga) 