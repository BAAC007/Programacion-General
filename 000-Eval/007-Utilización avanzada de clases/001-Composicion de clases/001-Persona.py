class Persona():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion

    def dameDatos(self):
        return self.nombre + self.apellidos
    
class Profesor(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)

class Alumnos(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)

class AlumnoOnline(Alumnos):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)
    
class AlumnoPresencial(Alumnos):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)


alumno1 = AlumnoPresencial("Bryan ", "Avila", "Info@avila.com", "Direccion")
print(alumno1.dameDatos())

profesor1 = Profesor("Jose Vicente ","Carratala","info@jocarsa.com","Direccion")
print(profesor1.dameDatos())