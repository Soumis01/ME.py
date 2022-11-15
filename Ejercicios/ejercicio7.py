''' Ejercico 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre
 por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
 de masa corporal calculado redondeado con dos decimales. '''

# Pregunta al usuario
peso = input("¿Cuál es tu peso en kg? ") 
estatura = input("¿Cuál es tu estatura en metros? ")

# Obtiene datos y los hace una ecuacion 
imc = round(float(peso)/float(estatura)**2,2)

print("Tu índice de masa corporal es " + str(imc)) # Imprime el resultado