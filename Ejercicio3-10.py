# Jesús Ramírez.

# Realizar un programa que imprima por pantalla la estación del
# usuario dependiendo de la información que ingrese.

# Pedimos el emisferio al usuario.
actividad10_emisferio = input("Ingrese el emisferio en que se encuentra. (N)orte o (S)ur. ")

# Se verifica el valor ingresado. Si no es de los pedidos, no se
# ejecuta el resto del programa; si lo es, continúa.
if actividad10_emisferio == "N" or actividad10_emisferio == "n" or actividad10_emisferio == "S" or actividad10_emisferio == "s":
    # Pedimos el día y el mes de la localidad del usuario.
    actividad10_dia, actividad10_mes = map(int, input("Ingrese el día y el mes de su localidad, en ese mismo órden. Sepárelos con un espacio. ").split())

    if actividad10_dia <= 31 and actividad10_dia >= 1 and actividad10_mes <= 12 and actividad10_mes >= 1:
        # Seguimos un ciclo en el que primero revisamos la fecha
        # que encaje con las fechas de cada temporada, luego revisa
        # el emisferio para finalmente imprimir el resultado.
        if (actividad10_mes, actividad10_dia) >= (12, 21) or (actividad10_mes, actividad10_dia) <= (3, 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es invierno.")
            else:
                print("Es verano.")

        elif (actividad10_mes == 3 and actividad10_dia >= 21) or (actividad10_mes in [4, 5]) or (actividad10_mes == 6 and actividad10_dia <= 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es primavera.")
            else:
                print("Es otoño.")

        elif (actividad10_mes == 6 and actividad10_dia >= 21) or (actividad10_mes in [7, 8]) or (actividad10_mes == 9 and actividad10_dia <= 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es verano.")
            else:
                print("Es invierno.")

        elif (actividad10_mes == 9 and actividad10_dia >= 21) or (actividad10_mes in [10, 11]) or (actividad10_mes == 12 and actividad10_dia <= 20):
            if actividad10_emisferio == "N" or actividad10_emisferio == "n":
                print("Es otoño.")
            else:
                print("Es primavera.")

    else:
        print("Se ha detectado un valor inválido en la fecha o el mes.")
else:
    print("El valor de emisferio ingresado es inválido.")
