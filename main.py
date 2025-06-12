#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aplicación principal para demostrar el uso de las clases Persona y Empleado.

Este módulo crea instancias de las clases Persona y Empleado, y muestra
su información en consola para demostrar la funcionalidad de herencia
y encapsulamiento en Python.

Autor: Mauricio Rivero
Fecha: 2024
comando de arranque: python3 main.py
"""

from datetime import date
from persona import Persona
from empleado import Empleado

class AplicacionPrincipal:
    """
    Clase principal que ejecuta la aplicación de demostración.
    
    Esta clase contiene métodos para crear objetos de tipo Persona y Empleado,
    y mostrar su información en consola.
    """
    
    def __init__(self):
        """
        Constructor de la clase AplicacionPrincipal.
        """
        self.personas = []  # Lista para almacenar objetos Persona
        self.empleados = []  # Lista para almacenar objetos Empleado
    
    def crear_personas(self):
        """
        Crea tres objetos de la clase Persona con datos de ejemplo.
        
        Este método instancia tres personas con información diferente
        y las almacena en la lista de personas.
        """
        print("=== CREANDO OBJETOS DE LA CLASE PERSONA ===")
        print()
        
        # Crear primera persona
        persona1 = Persona(
            id=1,
            nombre="María",
            apellido="González",
            fecha_nacimiento=date(1990, 5, 15),
            telefono="3001234567",
            correo="maria.gonzalez@email.com"
        )
        
        # Crear segunda persona
        persona2 = Persona(
            id=2,
            nombre="Carlos",
            apellido="Rodríguez",
            fecha_nacimiento=date(1985, 8, 22),
            telefono="3009876543",
            correo="carlos.rodriguez@email.com"
        )
        
        # Crear tercera persona
        persona3 = Persona(
            id=3,
            nombre="Ana",
            apellido="Martínez",
            fecha_nacimiento=date(1992, 12, 8),
            telefono="3005551234",
            correo="ana.martinez@email.com"
        )
        
        # Agregar personas a la lista
        self.personas = [persona1, persona2, persona3]
        
        print("✓ Se han creado 3 objetos de la clase Persona exitosamente.")
        print()
    
    def crear_empleados(self):
        """
        Crea tres objetos de la clase Empleado con datos de ejemplo.
        
        Este método instancia tres empleados con información diferente
        y los almacena en la lista de empleados.
        """
        print("=== CREANDO OBJETOS DE LA CLASE EMPLEADO ===")
        print()
        
        # Crear primer empleado
        empleado1 = Empleado(
            id=101,
            nombre="Luis",
            apellido="Pérez",
            fecha_nacimiento=date(1988, 3, 10),
            telefono="3001111111",
            correo="luis.perez@empresa.com",
            rol="Desarrollador de Software",
            responsabilidad="Desarrollo de aplicaciones web y móviles",
            salario=4500000.0
        )
        
        # Crear segundo empleado
        empleado2 = Empleado(
            id=102,
            nombre="Sandra",
            apellido="López",
            fecha_nacimiento=date(1987, 7, 25),
            telefono="3002222222",
            correo="sandra.lopez@empresa.com",
            rol="Gerente de Proyectos",
            responsabilidad="Coordinación y seguimiento de proyectos tecnológicos",
            salario=6200000.0
        )
        
        # Crear tercer empleado
        empleado3 = Empleado(
            id=103,
            nombre="Diego",
            apellido="Ramírez",
            fecha_nacimiento=date(1991, 11, 14),
            telefono="3003333333",
            correo="diego.ramirez@empresa.com",
            rol="Analista de Datos",
            responsabilidad="Análisis estadístico y creación de reportes",
            salario=3800000.0
        )
        
        # Agregar empleados a la lista
        self.empleados = [empleado1, empleado2, empleado3]
        
        print("✓ Se han creado 3 objetos de la clase Empleado exitosamente.")
        print()
    
    def mostrar_personas(self):
        """
        Muestra la información de todas las personas creadas.
        
        Este método recorre la lista de personas y muestra su información
        completa utilizando el método mostrar_informacion().
        """
        print("=== INFORMACIÓN DE LAS PERSONAS ===")
        print()
        
        for i, persona in enumerate(self.personas, 1):
            print(f"--- PERSONA {i} ---")
            print(persona.mostrar_informacion())
            print()
    
    def mostrar_empleados(self):
        """
        Muestra la información de todos los empleados creados.
        
        Este método recorre la lista de empleados y muestra su información
        completa utilizando el método mostrar_informacion().
        """
        print("=== INFORMACIÓN DE LOS EMPLEADOS ===")
        print()
        
        for i, empleado in enumerate(self.empleados, 1):
            print(f"--- EMPLEADO {i} ---")
            print(empleado.mostrar_informacion())
            print(f"Salario anual: ${empleado.calcular_salario_anual():,.2f}")
            print()
    
    def demostrar_setters_getters(self):
        """
        Demuestra el uso de los métodos setters y getters.
        
        Este método modifica algunos atributos usando setters y luego
        los muestra usando getters para demostrar su funcionamiento.
        """
        print("=== DEMOSTRACIÓN DE SETTERS Y GETTERS ===")
        print()
        
        if self.personas and self.empleados:
            # Demostrar con una persona
            persona = self.personas[0]
            print(f"Información original de {persona.get_nombre()}:")
            print(f"Teléfono: {persona.get_telefono()}")
            print(f"Correo: {persona.get_correo()}")
            print()
            
            # Modificar usando setters
            persona.set_telefono("3007777777")
            persona.set_correo("maria.gonzalez.nuevo@email.com")
            
            print("Después de usar setters:")
            print(f"Nuevo teléfono: {persona.get_telefono()}")
            print(f"Nuevo correo: {persona.get_correo()}")
            print()
            
            # Demostrar con un empleado
            empleado = self.empleados[0]
            print(f"Información original de {empleado.get_nombre()}:")
            print(f"Rol: {empleado.get_rol()}")
            print(f"Salario: ${empleado.get_salario():,.2f}")
            print()
            
            # Modificar usando setters
            empleado.set_rol("Desarrollador Senior")
            empleado.set_salario(5200000.0)
            
            print("Después de usar setters:")
            print(f"Nuevo rol: {empleado.get_rol()}")
            print(f"Nuevo salario: ${empleado.get_salario():,.2f}")
            print()
    
    def ejecutar(self):
        """
        Método principal que ejecuta toda la aplicación.
        
        Este método coordina la ejecución de todos los procesos:
        creación de objetos, muestra de información y demostración
        de funcionalidades.
        """
        print("=" * 60)
        print("    SISTEMA DE GESTIÓN DE PERSONAS Y EMPLEADOS")
        print("=" * 60)
        print()
        
        # Crear objetos
        self.crear_personas()
        self.crear_empleados()
        
        # Mostrar información
        self.mostrar_personas()
        self.mostrar_empleados()
        
        # Demostrar setters y getters
        self.demostrar_setters_getters()
        
        print("=" * 60)
        print("         APLICACIÓN EJECUTADA EXITOSAMENTE")
        print("=" * 60)

def main():
    """
    Función principal del programa.
    
    Esta función crea una instancia de AplicacionPrincipal
    y ejecuta el programa completo.
    """
    app = AplicacionPrincipal()
    app.ejecutar()

# Punto de entrada del programa
if __name__ == "__main__":
    main() 