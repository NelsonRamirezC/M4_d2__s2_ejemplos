class Direccion:
    def __init__(self, calle, ciudad, pais):
        self.calle = calle
        self.ciudad = ciudad
        self.pais = pais

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"

class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}"