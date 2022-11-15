''' Ejercico 8
Escribir un programa que pida al usuario dos números enteros y muestre por 
pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto 
de la división entera respectivamente. '''

# Pregunta al usuario
n = int(input('Escribe el primer numero: '));
m = int(input('Escribeel segundo nuemro: '));

# Como c va hacer el resultado de consinte tenemos que usar su operador y r
# es el resultado de residual
c = n/m;
r = n%m;

print('El consiten es : ' + str(c) + '\n\r''El residual es: ' +  str(r));
