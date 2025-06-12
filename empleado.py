from persona import Persona

class Empleado(Persona):
    """
    Clase que representa un empleado, heredando de la clase Persona.
    
    Atributos heredados:
        id (int): Identificador único de la persona
        nombre (str): Nombre de la persona
        apellido (str): Apellido de la persona
        fecha_nacimiento (date): Fecha de nacimiento de la persona
        telefono (str): Número de teléfono de la persona
        correo (str): Correo electrónico de la persona
    
    Atributos propios:
        rol (str): Rol o cargo del empleado en la empresa
        responsabilidad (str): Descripción de las responsabilidades del empleado
        salario (float): Salario del empleado
    """
    
    def __init__(self, id, nombre, apellido, fecha_nacimiento, telefono, correo, rol, responsabilidad, salario):
        """
        Constructor de la clase Empleado.
        
        Args:
            id (int): Identificador único de la persona
            nombre (str): Nombre de la persona
            apellido (str): Apellido de la persona
            fecha_nacimiento (date): Fecha de nacimiento de la persona
            telefono (str): Número de teléfono de la persona
            correo (str): Correo electrónico de la persona
            rol (str): Rol o cargo del empleado en la empresa
            responsabilidad (str): Descripción de las responsabilidades del empleado
            salario (float): Salario del empleado
        """
        # Llamar al constructor de la clase padre (Persona)
        super().__init__(id, nombre, apellido, fecha_nacimiento, telefono, correo)
        
        # Atributos específicos del empleado
        self._rol = rol
        self._responsabilidad = responsabilidad
        self._salario = salario
    
    # Getters (métodos para obtener los valores de los atributos específicos del empleado)
    
    def get_rol(self):
        """
        Obtiene el rol del empleado.
        
        Returns:
            str: El rol del empleado
        """
        return self._rol
    
    def get_responsabilidad(self):
        """
        Obtiene la responsabilidad del empleado.
        
        Returns:
            str: La responsabilidad del empleado
        """
        return self._responsabilidad
    
    def get_salario(self):
        """
        Obtiene el salario del empleado.
        
        Returns:
            float: El salario del empleado
        """
        return self._salario
    
    # Setters (métodos para establecer los valores de los atributos específicos del empleado)
    
    def set_rol(self, rol):
        """
        Establece el rol del empleado.
        
        Args:
            rol (str): El nuevo rol del empleado
        """
        self._rol = rol
    
    def set_responsabilidad(self, responsabilidad):
        """
        Establece la responsabilidad del empleado.
        
        Args:
            responsabilidad (str): La nueva responsabilidad del empleado
        """
        self._responsabilidad = responsabilidad
    
    def set_salario(self, salario):
        """
        Establece el salario del empleado.
        
        Args:
            salario (float): El nuevo salario del empleado
        """
        self._salario = salario
    
    def mostrar_informacion(self):
        """
        Muestra la información completa del empleado, incluyendo la información heredada de Persona.
        
        Returns:
            str: Cadena con toda la información del empleado
        """
        informacion_persona = super().mostrar_informacion()
        informacion_empleado = (f"Rol: {self._rol}\n"
                               f"Responsabilidad: {self._responsabilidad}\n"
                               f"Salario: ${self._salario:,.2f}")
        return f"{informacion_persona}\n{informacion_empleado}"
    
    def calcular_salario_anual(self):
        """
        Calcula el salario anual del empleado.
        
        Returns:
            float: El salario anual (salario mensual * 12)
        """
        return self._salario * 12
    
    def __str__(self):
        """
        Representación en cadena del empleado.
        
        Returns:
            str: Representación del empleado
        """
        return f"{self._nombre} {self._apellido} - {self._rol} (ID: {self._id})" 