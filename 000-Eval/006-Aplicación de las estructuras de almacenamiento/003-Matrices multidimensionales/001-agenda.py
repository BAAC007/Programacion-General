import pickle
agenda = []

try:
    archivo = open("agenda.bin",'rb')
    agenda = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo de datos")

while True:
    print("Selecciona una opcion: ")
    print("1.-Insertar un registro")
    print("2.-Leer registros")
    print("3.-Guardar registros")
    opcion = int(input("Opción escogida: "))

    if opcion == 1:
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu teléfono: ")
        agenda.append([nombre,apellidos,email,telefono])

    elif opcion == 2:
        identificador = 0
        for registros in agenda:
            print("Este es la persona registrada con ID:",identificador)
            print(agenda)
            identificador += 1

    elif opcion == 3:
        archivo = open("agenda.bin",'wb')
        pickle.dump(agenda,archivo)
        archivo.close()