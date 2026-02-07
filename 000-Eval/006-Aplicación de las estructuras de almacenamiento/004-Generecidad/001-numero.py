numeros = [6,2,8,"3","cero","5"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
  for numero in numeros:
    try:         
      numero = int(numero)
      print(numero * 2)
    except:   
      centinela = False
      
      for i in range(0,len(numeros_etiquetas)):
        if numero == numeros_etiquetas[i]:
          print(i*2)
          centinela = True
      if centinela == False:
        print("Se ha intentado pero no se ha logrado.")
        
calculaDoble()