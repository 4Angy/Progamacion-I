##Ejercicio2.2
# solicitar su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
#Solicitud al usuario
nota=int(input("Ingrese su nota: "))
#Condicional compuesto
if nota>=0 and nota<=10: #Validacion de nota
 if nota>=6:
    print("Aprobado")
 else:
    print("Desaprobado")
else:
    print("Nota no valida")

print("Fin del programa")