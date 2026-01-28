numeros = [
    1,
    2,
    "3",
    4,
    "cinco"
]
print(numeros)
numeros_etiquetas = ["cero", "uno", "dos", "tres", "cuatro"," cinco"]
def calculaDoble():
    for numero in numeros:
        #Primero intento convertir
        try:
            numero = int(numero)
            print(numero * 2)
        #Intenta buscar el valor en la lista de numeros
        except:
            for i in range(0,len(numeros_etiquetas)):
                if numero == numeros_etiquetas[i]:
                    print(i * 2)

calculaDoble()