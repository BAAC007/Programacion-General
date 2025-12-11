<!-- IMPORTANTE: Este es el index de admin -->
<!doctype html>
<html lang="es">
	<head>
  	<title>El Perol - Noticias tecnológicas</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
    <style>
    	body,html{width:100%;height:100%;padding:0px;margin:0px;background:teal;}
      body{display:flex;justify-content:center;align-items:center;}
      form{display:flex;flex-direction:column;gap:20px;padding:20px;background:white;}
    </style>
  </head>
  <body>
  	<form action="procesalogin.php" method="POST">
    	<input type="text" name="usuario" placeholder="usuario">
      <input type="password" name="contrasena" placeholder="contraseña">
      <input type="submit">
    </form>
  </body>
</html>
