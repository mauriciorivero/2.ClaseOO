from datetime import date

class Persona:
    """
    Clase que representa una persona con información básica personal.
    
    Atributos:
        id (int): Identificador único de la persona
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
        fecha_nacimiento (date): Fecha de nacimiento de la persona
        telefono (str): Número de teléfono de la persona
        correo (str): Correo electrónico de la persona
    """
    
    def __init__(self, id, nombre, apellido, fecha_nacimiento, telefono, correo):
        """
        Constructor de la clase Persona.
        
        Args:
            id (int): Identificador único de la persona
            nombre (str): Nombre de la persona
            apellido (str): Apellido de la persona
            fecha_nacimiento (date): Fecha de nacimiento de la persona
            telefono (str): Número de teléfono de la persona
            correo (str): Correo electrónico de la persona
        """
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._telefono = telefono
        self._correo = correo
    
    # Getters (métodos para obtener los valores de los atributos)
    
    def get_id(self):
        """
        Obtiene el identificador de la persona.
        
        Returns:
            int: El identificador de la persona
        """
        return self._id
    
    def get_nombre(self):
        """
        Obtiene el nombre de la persona.
        
        Returns:
            str: El nombre de la persona
        """
        return self._nombre
    
    def get_apellido(self):
        """
        Obtiene el apellido de la persona.
        
        Returns:
            str: El apellido de la persona
        """
        return self._apellido
    
    def get_fecha_nacimiento(self):
        """
        Obtiene la fecha de nacimiento de la persona.
        
        Returns:
            date: La fecha de nacimiento de la persona
        """
        return self._fecha_nacimiento
    
    def get_telefono(self):
        """
        Obtiene el teléfono de la persona.
        
        Returns:
            str: El teléfono de la persona
        """
        return self._telefono
    
    def get_correo(self):
        """
        Obtiene el correo electrónico de la persona.
        
        Returns:
            str: El correo electrónico de la persona
        """
        return self._correo
    
    # Setters (métodos para establecer los valores de los atributos)
    
    def set_id(self, id):
        """
        Establece el identificador de la persona.
        
        Args:
            id (int): El nuevo identificador de la persona
        """
        self._id = id
    
    def set_nombre(self, nombre):
        """
        Establece el nombre de la persona.
        
        Args:
            nombre (str): El nuevo nombre de la persona
        """
        self._nombre = nombre
    
    def set_apellido(self, apellido):
        """
        Establece el apellido de la persona.
        
        Args:
            apellido (str): El nuevo apellido de la persona
        """
        self._apellido = apellido
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        """
        Establece la fecha de nacimiento de la persona.
        
        Args:
            fecha_nacimiento (date): La nueva fecha de nacimiento de la persona
        """
        self._fecha_nacimiento = fecha_nacimiento
    
    def set_telefono(self, telefono):
        """
        Establece el teléfono de la persona.
        
        Args:
            telefono (str): El nuevo teléfono de la persona
        """
        self._telefono = telefono
    
    def set_correo(self, correo):
        """
        Establece el correo electrónico de la persona.
        
        Args:
            correo (str): El nuevo correo electrónico de la persona
        """
        self._correo = correo
    
    def mostrar_informacion(self):
        """
        Muestra la información completa de la persona.
        
        Returns:
            str: Cadena con toda la información de la persona
        """
        return (f"ID: {self._id}\n"
                f"Nombre: {self._nombre}\n"
                f"Apellido: {self._apellido}\n"
                f"Fecha de nacimiento: {self._fecha_nacimiento}\n"
                f"Teléfono: {self._telefono}\n"
                f"Correo: {self._correo}")
    
    def __str__(self):
        """
        Representación en cadena de la persona.
        
        Returns:
            str: Representación de la persona
        """
        return f"{self._nombre} {self._apellido} (ID: {self._id})" 