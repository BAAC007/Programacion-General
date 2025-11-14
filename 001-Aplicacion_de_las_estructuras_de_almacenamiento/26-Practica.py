print("Biblioteca V0.1")
import json # Para usar la libreria tengo que importarla

biblioteca = []

while True:
    print("Selecciona una opcion: ")
    print("1.Añadir un libro.")
    print("2.Ver libros")
    opcion = int(input("tu opcion: "))

    if opcion == 1:
        print("Añadimos un libros a la biblioteca:")
        nombre = input("Indica el nombre del libro: ")
        copias = input("Indica las copias que hay del libro: ")
        biblioteca.append({"nombre":nombre, "copias":copias})
        archivo = open("Biblioteca.json", "w") #Abro un archivo
        json.dump(biblioteca, archivo) #Guardo en json
        archivo.close() #Cierro el archivo

    elif opcion == 2:
        print("listamos los elementos de la lista")
        for libros in biblioteca:
            print("Libro:", libros['nombre'])
            print("Copias:", libros['copias'])
            print("--------------------------------")