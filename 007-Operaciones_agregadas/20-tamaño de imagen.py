from PIL import Image

imagen = Image.open("/var/www/html/MI_AREA/Programacion_2do_T/007-Operaciones_agregadas/imagen.jfif")

tamanio = imagen.size
print(tamanio)

pixel1 = imagen.getpixel((0, 0))

print(pixel1)
