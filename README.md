# Sistema de Gestión de Personas y Empleados

## 📋 Descripción

Este proyecto es una aplicación de Python que implementa un sistema de gestión de personas y empleados utilizando conceptos de **Programación Orientada a Objetos (POO)**. El sistema demuestra el uso de herencia, encapsulamiento y polimorfismo a través de dos clases principales: `Persona` y `Empleado`.

## 🚀 Características Principales

- ✅ **Clase Persona**: Gestiona información básica personal
- ✅ **Clase Empleado**: Hereda de Persona y añade información laboral
- ✅ **Encapsulamiento**: Atributos privados con métodos getters y setters
- ✅ **Herencia**: Empleado extiende la funcionalidad de Persona
- ✅ **Documentación completa**: Todos los métodos y atributos están documentados en español
- ✅ **Aplicación funcional**: Clase principal que demuestra el uso de las clases

## 📁 Estructura del Proyecto

```
2.ClaseOO/
│
├── persona.py          # Clase base Persona
├── empleado.py         # Clase Empleado (hereda de Persona)
├── main.py            # Aplicación principal
└── README.md          # Este archivo
```

## 🔧 Requisitos

- Python 3.6 o superior
- No se requieren librerías externas (solo módulos estándar de Python)

## 🏃‍♂️ Cómo Ejecutar

### Comando de arranque:
```bash
python3 main.py
```

### En sistemas Windows:
```bash
python main.py
```

## 📖 Descripción de las Clases

### Clase Persona (`persona.py`)

**Atributos:**
- `id` (int): Identificador único de la persona
- `nombre` (str): Nombre de la persona
- `apellido` (str): Apellido de la persona
- `fecha_nacimiento` (date): Fecha de nacimiento
- `telefono` (str): Número de teléfono
- `correo` (str): Correo electrónico

**Métodos principales:**
- Getters y setters para todos los atributos
- `mostrar_informacion()`: Muestra toda la información de la persona
- `__str__()`: Representación en cadena de la persona

### Clase Empleado (`empleado.py`)

**Hereda todos los atributos de Persona y añade:**
- `rol` (str): Cargo o rol del empleado
- `responsabilidad` (str): Descripción de responsabilidades
- `salario` (float): Salario mensual del empleado

**Métodos adicionales:**
- Getters y setters para los nuevos atributos
- `calcular_salario_anual()`: Calcula el salario anual
- `mostrar_informacion()`: Sobrescribe el método padre para incluir información laboral

### Clase AplicacionPrincipal (`main.py`)

**Funcionalidades:**
- Crea 3 objetos de la clase Persona
- Crea 3 objetos de la clase Empleado
- Muestra toda la información en consola
- Demuestra el uso de setters y getters

## 🎯 Ejemplo de Salida

Al ejecutar el programa, verás una salida similar a esta:

```
============================================================
    SISTEMA DE GESTIÓN DE PERSONAS Y EMPLEADOS
============================================================

=== CREANDO OBJETOS DE LA CLASE PERSONA ===

✓ Se han creado 3 objetos de la clase Persona exitosamente.

=== CREANDO OBJETOS DE LA CLASE EMPLEADO ===

✓ Se han creado 3 objetos de la clase Empleado exitosamente.

=== INFORMACIÓN DE LAS PERSONAS ===

--- PERSONA 1 ---
ID: 1
Nombre: María
Apellido: González
Fecha de nacimiento: 1990-05-15
Teléfono: 3001234567
Correo: maria.gonzalez@email.com

=== INFORMACIÓN DE LOS EMPLEADOS ===

--- EMPLEADO 1 ---
ID: 101
Nombre: Luis
Apellido: Pérez
Fecha de nacimiento: 1988-03-10
Teléfono: 3001111111
Correo: luis.perez@empresa.com
Rol: Desarrollador de Software
Responsabilidad: Desarrollo de aplicaciones web y móviles
Salario: $4,500,000.00
Salario anual: $54,000,000.00
```

## 🔍 Conceptos de POO Implementados

### 1. **Encapsulamiento**
- Los atributos están marcados como privados (prefijo `_`)
- Acceso controlado mediante métodos getters y setters
- Protección de la integridad de los datos

### 2. **Herencia**
- La clase `Empleado` hereda de la clase `Persona`
- Reutilización de código y extensión de funcionalidades
- Uso de `super()` para llamar métodos de la clase padre

### 3. **Polimorfismo**
- Sobrescritura del método `mostrar_informacion()`
- Diferentes comportamientos según el tipo de objeto

## 👨‍💻 Autor

**Mauricio Rivero**  
Fecha: 2024

## 📝 Notas de Desarrollo

- Todos los comentarios y documentación están en español
- El código sigue las convenciones de Python (PEP 8)
- Se incluye manejo de tipos de datos apropiados
- La aplicación es completamente funcional y lista para ejecutar

## 🤝 Contribuciones

Este es un proyecto educativo para demostrar conceptos de POO en Python. Si deseas contribuir o sugerir mejoras, eres bienvenido a hacerlo.

---

*Este proyecto forma parte del programa SENA 2025 - Tecnólogo en Análisis y Desarrollo de Software* 