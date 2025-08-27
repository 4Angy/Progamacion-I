#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.


contrasena = input("[Ingrese una contraseña de dentre 8 y 14 caracteres]:")

if( len(contrasena) < 8 or len(contrasena)>14 ):
    print("[Por favor, ingrese una contraseña de entre 8 y 14 caracteres]")
else:
    print("[Ha ingresado una contraseña correcta]")


#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

print(numeros_aleatorios)

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if(media > mediana and mediana > moda):
    print("[Sesgo positivo o a la derecha]")
elif(media < mediana and mediana < moda):
    print("[Sesgo negativo o a la izquierda]")
elif(mediana == media and media == moda):
    print("[Sin sesgo]")
else:
    print("[Ninguna de las anteriores]")