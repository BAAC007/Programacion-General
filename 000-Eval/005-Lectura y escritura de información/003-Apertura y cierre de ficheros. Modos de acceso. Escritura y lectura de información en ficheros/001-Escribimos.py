"""

Empezamos con el primer paso de este ejercicio, abriendo y escribiendo
un poco sobre los hobbies que practico en un archivo .txt y cerramos el archivo.

Continuamos con el segundo paso que es: abrir nuevamente el archivo .txt y
añadimos cuando fue la ultima vez que practique uno de mis hobbies y cerramos
el archivo.

Y por ultimos paso abrimos nuevamente el archivo .txt para leer todas las lineas
que tenga utilizando un bucle for y despues de esto cerraremos el archivo.

"""

archivo = open("datos.txt","w")
archivo.write("Me gusta ir a entrenar y estudiar en la comodidad de mi hogar.")
archivo.close()


archivo = open("datos.txt","a")
archivo.write("La ultima vez que entrené fue hoy por la tarde.")
archivo.close()


archivo = open("datos.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    print(linea)
archivo.close