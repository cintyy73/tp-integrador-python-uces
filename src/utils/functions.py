"""
Módulo de funciones utilitarias
================================

Este módulo contiene funciones auxiliares reutilizables en todo el proyecto.
Centralizar estas funciones evita la duplicación de código y facilita
el mantenimiento (principio DRY - Don't Repeat Yourself).

Funciones disponibles:
- print_header(): Encabezados formateados con caracteres especiales
- clear_screen(): Limpia la pantalla de la terminal
- pause(): Pausa la ejecución esperando Enter
- confirm_action(): Solicita confirmación s/n
- print_separator(): Imprime líneas separadoras
- print_success/error/warning(): Mensajes formateados con emojis
"""

import os


def print_header(title):
    """
    Imprime un encabezado bonito y centrado en la terminal.
    Usa caracteres especiales Unicode para crear un marco decorativo.
    
    Parámetros:
        title (str): El texto a mostrar en el encabezado
    
    Ejemplo:
        print_header("Bienvenido")
        
        Salida:
        ╔══════════════════════════════════════╗
        ║             Bienvenido               ║
        ╚══════════════════════════════════════╝
    """
    width = 40  # Ancho fijo del encabezado
    
    # Línea superior del marco
    print("╔" + "═" * (width - 2) + "╗")
    
    # center() es un método de string que centra el texto
    # añadiendo espacios a los lados según sea necesario
    print("║" + title.center(width - 2) + "║")
    
    # Línea inferior del marco
    print("╚" + "═" * (width - 2) + "╝")
    print()  # Espacio extra después del encabezado


def clear_screen():
    """
    Limpia la pantalla de la terminal.
    
    Detecta el sistema operativo para usar el comando correcto:
    - Windows (nt): usa 'cls'
    - Unix/Linux/Mac (posix): usa 'clear'
    
    Retorna:
        None
    """
    # os.name retorna 'nt' en Windows, 'posix' en Unix/Linux/Mac
    # os.system() ejecuta un comando del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(message="\nPresione Enter para continuar..."):
    """
    Pausa la ejecución esperando que el usuario presione Enter.
    Útil para que el usuario pueda leer mensajes antes de continuar.
    
    Parámetros:
        message (str): Mensaje a mostrar (opcional)
    
    Retorna:
        None
    """
    input(message)


def confirm_action(message="¿Está seguro? (s/n): "):
    """
    Solicita confirmaación al usuario con respuesta s/n.
    
    Parámetros:
        message (str): Mensaje de confirmación a mostrar
    
    Retorna:
        bool: True si el usuario responde 's', False en caso contrario
    
    Ejemplo:
        if confirm_action("¿Desea eliminar este registro?"):
            # Realizar la acción
    """
    # lower() convierte a minúsculas, strip() quita espacios en blanco
    response = input(message).lower().strip()
    return response == 's'


def print_separator(char="-", length=50):
    """
    Imprime una línea separadora visual.
    
    Parámetros:
        char (str): Carácter a usar para la línnea (por defecto '-')
        length (int): Longitud de la línea (por defecto 50)
    
    Ejemplo:
        print_separator()  # Imprime: --------------------------------------------------
        print_separator("=", 30)  # Imprime: ==============================
    """
    print(char * length)


def print_success(message):
    """
    Imprime un mensaje de éxito con formato y emoji.
    
    Parámetros:
        message (str): Mensaje a mostrar
    
    Ejemplo:
        print_success("Registro guardado correctamente")
        # Salida: ✓ Registro guardado correctamente
    """
    print(f"\n✓ {message}")


def print_error(message):
    """
    Imprime un mensaje de error con formato y emoji.
    
    Parámetros:
        message (str): Mensaje a mostrar
    
    Ejemplo:
        print_error("No se pudo conectar a la base de datos")
        # Salida: ✗ No se pudo conectar a la base de datos
    """
    print(f"\n✗ {message}")


def print_warning(message):
    """
    Imprime un mensaje de advertencia con formato y emoji.
    
    Parámetros:
        message (str): Mensaje a mostrar
    
    Ejemplo:
        print_warning("Esta acción no se puede deshacer")
        # Salida: ⚠ Esta acción no se puede deshacer
    """
    print(f"\n⚠ {message}")