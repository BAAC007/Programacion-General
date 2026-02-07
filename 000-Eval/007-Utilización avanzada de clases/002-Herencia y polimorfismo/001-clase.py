class Persona():
    def __init__(self,nombre,apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def dameDatos(self):
        return self.nombre + self.apellidos
    
class Profesor(Persona):
    def __init__(self, nombre, apellidos):
        super().__init__(nombre, apellidos)

    def dameDatos(self):
        return "Profesor: " + self.nombre + self.apellidos

class Alumno(Persona):
    def __init__(self, nombre, apellidos, email):
        super().__init__(nombre, apellidos)

    def dameDatos(self):
        return "Alumno: " + self.nombre + " " + self.apellidos    


alumno1 = Alumno("Bryan", "Avila", "Info@avila.com")
print(alumno1.dameDatos())

profesor1 = Profesor("Jose Vicente","Carratala")
print(profesor1.dameDatos())