import pickle

menu = []

while True:
    print("Opciones:")
    print("1.-Introducir nueva comida en el menu")
    print("2.-Listar comidas en el menu")
    print("3.-Guardar en archivo")
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
