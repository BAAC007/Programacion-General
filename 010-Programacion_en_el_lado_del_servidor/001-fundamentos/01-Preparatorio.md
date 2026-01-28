PHP es un lenguaje del lado del servidor
requiere que tengamos un servidor preparado

formas fáciles de preparar un servidor

en linux(la buena):
terminal:
sudo apt install apache2 (instalar apache)
sudo apt install php (para instalar php sobre apache)
sudo chdmod 777 -R /var/www/html (para dar permisos a la carpeta) 

y a partir de ese momento:
1.-todos los archivos se meten dentro de /var/www/html
2.-en el navegador ponemos https://localhost/....

en windows (la forma mala)
descargamos XAMPP: https://www.apachefriends.org/es/index.html
instalamos XAMPP
en el panel de control de XAMPP arrancamos de momento solo apache

y apartir de ese momento:
1.-todos los archivos se meten dentro de C:/xampp/htdocs
2.-en el navegador ponemos https://localhost//....