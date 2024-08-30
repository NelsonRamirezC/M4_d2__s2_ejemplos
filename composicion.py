class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_informacion(self):
        habitaciones_info = ", ".join(str(habitacion) for habitacion in self.habitaciones)
        return f"Dirección: {self.direccion}, Habitaciones: {habitaciones_info}"