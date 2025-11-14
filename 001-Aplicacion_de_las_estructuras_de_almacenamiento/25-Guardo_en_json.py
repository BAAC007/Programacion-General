print("Lista de compra V0.1")
import json # Para usar la libreria tengo que importarla

lista_de_la_compra = []

while True:
    print("Selecciona una opcion: ")
    print("1.Añadir elementos a la lista.")
    print("2.Leer la lista")
    opcion = int(input("tu opcion: "))

    if opcion == 1:
        print("Añadimos un elemento a la lista:")
        nombre = input("Indica el nombre del producto: ")
        cantidad = input("Indica la cantidad del producto: ")
        lista_de_la_compra.append({"nombre":nombre, "cantidad":cantidad})
        archivo = open("lista.json", "w") #Abro un archivo
        json.dump(lista_de_la_compra, archivo) #Guardo en json
        archivo.close() #Cierro el archivo

    elif opcion == 2:
        print("listamos los elementos de la lista")
        for productos in lista_de_la_compra:
            print("Producto:", productos['nombre'])
            print("Cantidad:", productos['cantidad'])
            print("--------------------------------")