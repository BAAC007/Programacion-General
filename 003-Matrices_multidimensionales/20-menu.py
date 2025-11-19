import pickle
agenda = []

while True:
    print("Selecciona una opcion: ")
    print("1.-Insertar un registro")
    print("2.-Leer un registro")
    print("3.-Guardar registros")
    print("4.-Eliminar un registro")
    opcion = int(input("Ingrese su opcion: "))
    #Insertar
    if opcion == 1:
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu telefono: ")
        agenda.append([nombre,apellidos,email,telefono])

    #Imprimir
    elif opcion == 2:
        print(agenda)

    #Guardar
    elif opcion == 3:
        archivo = open("Agenda.bin", 'wb')
        pickle.dump(agenda,archivo)
        archivo.close()

    #Eliminar
    elif opcion == 4:
        eliminar = int(input("Ingresa el registro a eliminar: "))
        agenda.pop(eliminar)