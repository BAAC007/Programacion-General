#Empezamos creando un bucle while con el valor True
#Y hacemos un meno en el cual podremo elegir 2 opciones
#La primer para agregar a una persona nueva a la agenda
#Y la segunda para ver las personas que estan en la agenda



while True:
    print("Dime lo que quieres hacer: ")
    print("1.-Introduce un nuevo contacto")
    print("2.-Leer todos los contactos")
    opcion = int(input("Escoge tu opcion: "))

    if opcion == 1:
        nombre = input("Introduce el nombre de la persona: ")
        email = input("Introduce el email de la persona: ")
        archivo = open("agenda.txt", 'a')
        archivo.write(nombre+","+email+"\n")
        archivo.close()
        

    elif opcion == 2:
        archivo = open("archivo.txt",'r')
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
        archivo.close

