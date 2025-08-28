git push -u origin ejerciciosAngy
#ejercicio 7
palabraUsuario = input("Ingresa una palabra: \n")

#verificacion si cumple alguna condicion
if palabraUsuario[-1].lower() in "aeiou":
    print(palabraUsuario + "!")
#Si no..
else:
    print(palabraUsuario)

#ejercicio 8

#solicito el nombre
nombreUsuario = input("Hola!, Ingresa tu nombre: \n")
#menu de opciones
menuUsuario = input("Ingresa el numero correspondiente a como lo quieres ver: \n1.Mayúsculas \n2.Minusculas \n3.Primera mayuscula, resto minuscula\n")

#imprime segun la eleccion del usuario
if menuUsuario == "1": print(nombreUsuario.upper())
if menuUsuario == "2": print(nombreUsuario.lower())
if menuUsuario == "3": print(nombreUsuario.title()
