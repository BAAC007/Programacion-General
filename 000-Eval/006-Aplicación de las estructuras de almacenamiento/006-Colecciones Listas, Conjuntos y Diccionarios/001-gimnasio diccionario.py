gimnasio = {
    "nombre":"Gimnasio Fitness",
    "ubicación":"Calle Mayor, 123",
    "horarios":["Lunes a Viernes", "9:00 AM - 6:00 PM"],
    "tipo de ejercicios": "Funcional y Cardio",
}

equipo_futbol = {
    "nombre":"La Vinotinto",
    "ubicación":"Parque de los caobos, 3",
    "horarios":["Lunes, Miercoles y Viernes", "2:00 PM - 6:00 PM"],
    "tipo de ejercicios": "físico, técnico y táctico",
}

natacion = {
    "nombre":"Piscina techada del pueblo",
    "ubicación":"Centro Burjassot, 45",
    "horarios":["Lunes a Viernes", "7:00 AM - 8:00 PM"],
    "tipo de ejercicios": "Mariposa",
}


gimnasios = [gimnasio, equipo_futbol, natacion]

print(gimnasios[0]["nombre"])
print(gimnasios[1]["horarios"])