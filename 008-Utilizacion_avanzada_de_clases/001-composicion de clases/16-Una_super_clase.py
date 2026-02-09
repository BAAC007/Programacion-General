class Persona():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
    def dameDatos(self):
        return self.nombre+self.apellidos+self.email+self.direccion

class Profesor(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)
    
class Alumno(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)
    
        
alumno1 = Alumno("Bryan Alejandro ","Avila Castro ","info@Avila.com ","lamebotas")
print(alumno1.dameDatos())

profesor1 = Profesor("Juan"," Garcia ","juan@jocarsa.com ","jerusalem")
print(profesor1.dameDatos())