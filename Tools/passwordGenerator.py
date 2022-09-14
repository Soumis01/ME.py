import random
import string


# Primero importamos todas las letras del alfabeto y luego le sumamos los numeros 
caractares = string.ascii_letters + '1234567890'

password = ''

n = int(input('Coloca el numero de caracters: '))

# Creamos un bucle for para usar el randonw y tomar los caracteres de una manera aleatoria
for i in range (n):
    random_letter = random.choice (caractares)
    password = password + random_letter
print(password)