from PIL import Image

imagen = Image.open("imagen.jfif")

pixel1 = imagen.getpixel((0, 0))

print(pixel1)
