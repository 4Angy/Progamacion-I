# Jesús Ramírez.

# Escribir un programa que solicite al usuario su edad e imprima
# por pantalla si entra en la categoría de niño, adolescente,
# adulto joven o aldulto mayor.

actividad4_edad = int(input("Ingrese su edad. "))
if actividad4_edad > 0: # Pedimos la edad del usuario y pedimos la edad máxima de la categoría más baja, una por una.
    if actividad4_edad < 12:
        print("Niño: menores de 12 años.")
    elif actividad4_edad < 18:
        print("Adolescente: mayor de 11 años y menor de 18 años.")
    elif actividad4_edad < 30:
        print("Adulto joven: mayor de 17 años y menor de 30.")
    else:
        print("Adulto mayor: mayor de treinta años.")
else:
    print("Edad inválida.")
