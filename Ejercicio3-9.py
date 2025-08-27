#Ejercicio 3.9
#pedir al usuario la magnitud de un terremoto, clasifique la magnitud
#Solicitud al usuario
magnitud=float(input("Ingresa la magnitud del terremoto: ")) #Magnitud del terremoto
#Segun la escala de Richter
if magnitud>0:
 if magnitud<3.0:
    print("Muy leve (imperceptible)")
 elif 3.0<=magnitud<4.0:
    print("Leve (ligeramente perceptible)")
 elif 4.0<=magnitud<5.0:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
 elif 5.0<=magnitud<6.0:
    print("Fuerte (puede causar daños en estructuras débiles")
 elif 6.0<=magnitud<7.0:
    print("Muy fuerte (puede causar daños significativos)")
 else:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Valor no valido")
print("Fin del programa")
