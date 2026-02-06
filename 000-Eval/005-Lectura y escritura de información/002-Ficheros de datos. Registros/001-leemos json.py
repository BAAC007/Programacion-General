"""

Empezamos con importar la libreria json,
creamos una variable llamada 'archivo' para leer el archivo json
cargamos el contenido escribiendo el comando json.load(archivo) en la varible
'contenido', creamos un bucle for para visualizar la informacion linea por linea
del archivo json

"""

import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for linea in contenido:
    print("####### ARTICULO ########")
    print(linea['titulo'])
    print(linea['fecha'])
    print(linea['autor'])
    print(linea['contenido'])
    print("#########################")
    print("Excelente!,Ha leido exitosamente los articulos del blog🥳.")