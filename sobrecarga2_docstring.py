from multipledispatch import dispatch
#importante, en consola instalar previamente el módulo con comando pip install multipledispatch

class Persona:
    @dispatch()
    def __init__(self):
        """
        Constructor por defecto que inicializa las propiedades de la clase Persona.
        Las propiedades nombre, edad y ciudad son inicializadas con valores predeterminados:
        - nombre: cadena vacía
        - edad: 0
        - ciudad: cadena vacía
        """
        self.nombre = ""
        self.edad = 0
        self.ciudad = ""

    @dispatch(str, int)
    def __init__(self, nombre, edad):
        """
        Constructor que inicializa una instancia de Persona con un nombre y una edad.

        Parámetros:
        - nombre (str): El nombre de la persona.
        - edad (int): La edad de la persona.

        El atributo ciudad se mantiene con su valor predeterminado (cadena vacía).
        """
        self.__init__()
        self.nombre = nombre
        self.edad = edad
    
    @dispatch(str, str)
    def __init__(self, nombre, ciudad):
        """
        Constructor que inicializa una instancia de Persona con un nombre y una ciudad.

        Parámetros:
        - nombre (str): El nombre de la persona.
        - ciudad (str): La ciudad de residencia de la persona.

        El atributo edad se mantiene con su valor predeterminado (0).
        """
        self.__init__()
        self.nombre = nombre
        self.ciudad = ciudad
    
    @dispatch(str, int, str)
    def __init__(self, nombre, edad, ciudad):
        """
        Constructor que inicializa una instancia de Persona con un nombre, una edad y una ciudad.

        Parámetros:
        - nombre (str): El nombre de la persona.
        - edad (int): La edad de la persona.
        - ciudad (str): La ciudad de residencia de la persona.
        """
        self.__init__()
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad