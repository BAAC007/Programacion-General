import pickle

menu = []

while True:
    print("Opciones:")
    print("1.-Introducir nueva comida en el menu")
    print("2.-Listar comidas en el menu")
    print("3.-Guardar en archivo")
    print("4.-Cargar archivo")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        comida = input("Introduce el nombre de la comida que quieras añadir: ")
        menu.append(comida)
    elif opcion == 2:
        print("Hasta el momento tu comida es: ")
        for elemento in menu:
            print(elemento)
    elif opcion == 3:
        archivo = open("datos.txt", "wb") #Se escribe en binario
        pickle.dump(menu, archivo)
        archivo.close()
        print("Se ha guardado con exito🤟")
    elif opcion == 4:
        archivo = open("datos.txt", "rb") #Se carga el archivo binario
        menu = pickle.load(archivo) #Volcamos el archivo a la lista
        archivo.close()
        print("Los elementos guardados se han cargado correctamente💪")