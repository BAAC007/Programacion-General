import pickle

menu = []

try:
    archivo = open("comidas.bin",'rb')
    menu = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo de datos")

while True:
    
    print("Escoge una opción:")
    print("1.-Insertar una comida")
    print("2.-Listar comidas")
    print("3.-Guardar los alimentos")
    opcion = int(input("Escoge una opcion: "))
    
    if opcion == 1:
        nombre = input("Introduce el nombre de la comida: ")
        menu.append(nombre)

    elif opcion == 2:
        identificador = 0
        for alimentos in menu:
            print("Este es el cliente con ID:",identificador)
            print(alimentos)
            identificador += 1

    elif opcion == 3:
        archivo = open("comidas.bin",'wb')
        pickle.dump(menu,archivo)
        archivo.close()

    else:
        print("Opción no válida")