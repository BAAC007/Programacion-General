# pip3 install pillow --break-system-packages
from PIL import Image

imagen = Image.open("/var/www/html/MI_AREA/Programacion_2do_T/007-Operaciones_agregadas/imagen.jfif")

anchura,altura = imagen.size	

for x in range(0,anchura):	
    for y in range(0,altura):	
      pixel = imagen.getpixel((x, y))	
      # Primero leo los componentes de color
      rojo = pixel[0]
      verde = pixel[1]
      azul = pixel[2]
      # Ahora le subo el tono de color (aclaro)
      rojo += 20
      verde += 20
      azul += 20
      # Y sobreeescribo el valor
      pixel = (rojo,verde,azul)
    
imagen.save("modificado.jpg")