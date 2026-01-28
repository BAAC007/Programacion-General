persona = {
    "nombre":"Bryan Alejandro",
    "apellidos":"Avila Castro",
    "correo":"info@Avila.com",
    "edad":19,
    "telefonos":[
        {
            "tipo":"fijo",
            "numero":96123455
        },
        {
            "tipo":"movil",
            "numero":65456546
        }
    ]
}

print(persona)
print(persona["telefonos"][0]["numero"])