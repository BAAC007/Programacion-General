<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Tienda</title>
    <style>
        /* ===== Mobile-first enhancements ===== */
        @media (max-width: 768px) {

            body {
                font-size: 16px;
            }

            header h1 {
                margin: 0;
                font-size: 1.4rem;
            }

            main {
                padding: 10px;
            }

            section {
                margin-bottom: 20px;
            }

            h3 {
                margin-bottom: 10px;
                font-size: 1.2rem;
                text-align: center;
            }

            /* Products layout */
            #productos>div {
                display: flex;
                flex-direction: column;
                gap: 12px;
            }

            article {
                border: 1px solid #ddd;
                padding: 12px;
                border-radius: 8px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            article h4 {
                margin: 0;
                font-size: 1rem;
            }

            button {
                padding: 10px 14px;
                font-size: 1rem;
                border: none;
                border-radius: 6px;
                background: green;
                color: #fff;
                cursor: pointer;
            }

            button:active {
                transform: scale(0.97);
            }

            /* Client data form */
            section:last-of-type>div {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }

            input {
                padding: 10px;
                font-size: 1rem;
                border-radius: 6px;
                border: 1px solid #ccc;
                width: 100%;
                box-sizing: border-box;
            }

            #enviar {
                margin-top: 10px;
                padding: 12px;
                text-align: center;
                background: green;
                color: #fff;
                border-radius: 8px;
                font-size: 1rem;
                cursor: pointer;
            }

            #enviar:active {
                transform: scale(0.98);
            }

            footer {
                font-size: 0.85rem;
                padding: 8px;
            }
        }
    </style>
</head>

<body>
    <header>
        <h1>Mercadona</h1>
    </header>
    <main>
        <section id="Productos">
            <h3>Productos</h3>
            <div>
                <?php
                $host = "localhost";
                $user = "microtienda";
                $pass = "Microtienda$123";
                $db   = "microtienda";
                $conexion = new mysqli($host, $user, $pass, $db);
                $sql = "SELECT * FROM productos;";
                $resultado = $conexion->query($sql);
                while ($fila = $resultado->fetch_assoc()) {
                ?>
                    <article>
                        <h4><?= $fila['nombre'] ?></h4>
                        <button nombre="<?= $fila['nombre'] ?>"><?= $fila['precio'] ?>€</button>
                    </article>
                <?php } ?>
            </div>
        </section>
        <section>
            <h3>Datos del cliente</h3>
            <div>
                <input type="text" id="nombre" placeholder="nombre">
                <input type="text" id="apellidos" placeholder="apellidos">
                <input type="text" id="email" placeholder="email">
                <div id="enviar">Enviar pedido</div>
            </div>
        </section>
    </main>
    <footer>
        (c) 2026 Bryan Alejandro Avila Castro
    </footer>
</body>
<script>
    var fecha = new Date();
    var pedido = {
        cliente: {},
        productos: [],
        pedido: {
            "numero": Date.now(),
            "fecha": fecha.getFullYear() + "-" + (fecha.getMonth() + 1) + "-" + fecha.getDate()
        }
    };

    //Atrapa productos y los mete en el carro.
    let botones = document.querySelectorAll("button")
    botones.forEach(function(boton) {
        boton.onclick = function() {
            pedido.productos.push({
                "nombre": this.getAttribute("nombre"),
                "precio": this.textContent
            })
            console.log(pedido)
        }
    })

    //Atrapa los datos del cliente.
    let boton_enviar = document.querySelector("#enviar");
    boton_enviar.onclick = function() {
        let nombre_cliente = document.querySelector("#nombre").value;
        let apellidos_cliente = document.querySelector("#apellidos").value;
        let email_cliente = document.querySelector("#email").value;
        pedido.cliente = {
            "nombre": nombre_cliente,
            "apellidos": apellidos_cliente,
            "email": email_cliente
        }
        console.log(pedido)
        // Y los envio para guardar
        fetch("guardamongo.php?json=" + encodeURIComponent(JSON.stringify(pedido)))
    }
</script>

</html>