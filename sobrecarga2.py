from multipledispatch import dispatch
#importante, en consola instalar previamente el módulo con comando pip install multipledispatch

class Persona:
    @dispatch()
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.ciudad = ""

    @dispatch(str, int)
    def __init__(self, nombre, edad):
        self.__init__()
        self.nombre = nombre
        self.edad = edad
    
    @dispatch(str, str)
    def __init__(self, nombre, ciudad):
        self.__init__()
        self.nombre = nombre
        self.ciudad = ciudad
    
    @dispatch(str, int, str)
    def __init__(self, nombre, edad, ciudad):
        self.__init__()
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        
        
