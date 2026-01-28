<!doctype html>
<html>
	<head>
  	<link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
    <?php include "inc/conexion_bd.php"; ?>
    <nav>
    <?php include "controladores/poblar_menu.php" ?>
    </nav>
    <main>
      <table>
    <?php include "controladores/leer.php" ?>
      </table>
    </main>
  </body>
</html>