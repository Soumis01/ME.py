# Definimos la puntuacion, al empezar obviamente es 0
puntuacion = 0

# Preguntamos al usuario cuanto es 2 + 2 y guardamos la respuesta en la variable respuesta
respuesta = input("Cuanto es 2 + 2: ")

# Si la respuesta es correcta incrementamos la puntuacion
if respuesta == "4":
    puntuacion += 1
    print("Correcto")
else:
    print("Incorrecto") # Si es incorrecto mostramos un mensaje, pero no incrementamos la puntuacion

respuesta = input("Cuanto es 3 + 3: ")

if respuesta == "6":
    puntuacion += 1
    print("Correcto")
else:
    print("Incorrecto") # Si es incorrecto mostramos un mensaje, pero no incrementamos la puntuacion

respuesta = input("Cuanto es 4 + 4: ")

if respuesta == "8":
    puntuacion += 1
    print("Correcto")
else:
    print("Incorrecto") # Si es incorrecto mostramos un mensaje, pero no incrementamos la puntuacion

print(f"Tu puntuacion es: {puntuacion}/3") # Mostramos la puntuacion final