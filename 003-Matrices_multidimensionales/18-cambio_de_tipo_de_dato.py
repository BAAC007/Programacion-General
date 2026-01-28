tupla = ("Manzanas","Peras","Platanos")
#Necesito meter una fruta mas

lista = list(tupla) #convierto una tupla en una lista
print(tupla)
lista.append("Fresas")
print(lista)

#Ahora supongamos que tengo que volver a tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)